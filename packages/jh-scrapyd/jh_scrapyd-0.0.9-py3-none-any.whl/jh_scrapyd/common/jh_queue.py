from abc import ABC, abstractmethod
import time
import redis
import logging
from jh_scrapyd.common.utils import (
    str_decode,
    data_encode,
    data_decode
)


def _gen_key(arr, sep: str = ':') -> str:
    """生成 Redis 键"""
    return sep.join([str_decode(s) for s in arr])


class Queue(ABC):
    def __init__(self, storage, table: str = 'default', is_unified_queue: bool = False):
        """Initialize queue"""
        self.storage = storage
        self.table = table
        self.is_unified_queue = is_unified_queue
        self.now_time = int(time.time())

    @abstractmethod
    def put(self, z_key: str, key: str, data: dict, score: float = 1) -> bool:
        """Writes data with fractions"""

    @abstractmethod
    def pop(self, z_key: str, desc: bool = True):
        """Sort the columns as specified"""

    @abstractmethod
    def remove(self, z_key: str, key: str) -> bool:
        """Delete data from the queue"""

    @abstractmethod
    def list(self, z_key: str, desc: bool = True):
        """Get all queue data in order"""

    @abstractmethod
    def count(self, z_key: str) -> int:
        """Get number of queues"""

    @abstractmethod
    def clear(self, z_key: str):
        """Clear the specified collection data"""

    def score_weight(self, score: float = 1) -> int:
        """Calculate score weight"""
        return int(self.now_time * score)


class RedisQueue(Queue):
    SET_NAME = 'queue_set'
    HASH_NAME = 'queue_data'

    def put(self, z_key: str, key: str, data: dict, score: float = 1) -> bool:
        if not data:
            return False
        try:
            with self.storage.pipeline() as pipe:
                pipe.zadd(self._gen_set_key(z_key), {key: self.score_weight(score)})
                pipe.set(self._gen_hash_key(z_key, key), data_encode(data))
                pipe.execute()
            return True
        except redis.RedisError as e:
            logging.error(f"Error adding task to queue: {e}")
            return False

    def pop(self, z_key: str, desc: bool = True):
        try:
            ret = self.pop_by_set(z_key, desc)
            if not ret:
                return None

            key = ret[0][0]
            result = self.storage.get(self._gen_hash_key(z_key, key))
            self.remove(z_key, key)
            return data_decode(result)
        except redis.RedisError as e:
            logging.error(f"Error popping task from queue: {e}")
            return None

    def remove(self, z_key: str, key: str) -> bool:
        try:
            with self.storage.pipeline() as pipe:
                pipe.zrem(self._gen_set_key(z_key), key)
                pipe.delete(self._gen_hash_key(z_key, key))
                pipe.execute()
            return True
        except redis.RedisError as e:
            logging.error(f"Error removing task from queue: {e}")
            return False

    def list(self, z_key: str, desc: bool = True):
        try:
            z_key_str = self._gen_set_key(z_key)
            key_list = self.storage.zrange(z_key_str, 0, -1, desc, True)
            return [data_decode(self.storage.get(self._gen_hash_key(z_key, item[0]))) for item in key_list]
        except redis.RedisError as e:
            logging.error(f"Error listing tasks from queue: {e}")
            return []

    def count(self, z_key: str) -> int:
        try:
            return self.storage.zcard(self._gen_set_key(z_key))
        except redis.RedisError as e:
            logging.error(f"Error obtaining the number of queues: {e}")
            return 0

    def clear(self, z_key: str):
        try:
            self._clear_by_prefix(self._gen_set_key(z_key))
            self._clear_by_prefix(_gen_key([self.table, self.HASH_NAME, z_key]))
        except redis.RedisError as e:
            logging.error(f"Error clearing queue: {e}")

    def pop_by_set(self, z_key: str, desc: bool = True):
        return self.storage.zpopmax(self._gen_set_key(z_key)) if desc else self.storage.zpopmin(self._gen_set_key(z_key))

    def _clear_by_prefix(self, prefix: str) -> bool:
        try:
            cursor = 0
            while True:
                cursor, keys = self.storage.scan(cursor=cursor, match=f"{prefix}*", count=1000)
                if keys:
                    self.storage.delete(*keys)
                if cursor == 0:
                    break
            return True
        except redis.RedisError as e:
            logging.error(f"Error deleting specified key: {prefix}")
            return False

    def _gen_hash_key(self, z_key, key) -> str:
        return _gen_key([self.table, self.HASH_NAME, z_key, key])

    def _gen_set_key(self, z_key) -> str:
        key_arr = [self.table, self.SET_NAME]
        if not self.is_unified_queue:
            # Different projects use different queues
            key_arr.append(z_key)
        return _gen_key(key_arr)

    def retry_failed_task(self, z_key: str, key: str, data: dict, score: float = 1, max_retries: int = 3):
        retry_count = data.get('retry_count', 0)
        if retry_count < max_retries:
            data['retry_count'] = retry_count + 1
            self.put(z_key, key, data, score)
        else:
            logging.error(f"Max retries reached for task {key}")



if __name__ == '__main__':
    redis_client = redis.StrictRedis(
        host='127.0.0.1',
        port=6379,
        db=0
    )
    test_queue = RedisQueue(redis_client, is_unified_queue=False)

    z_keys = 'demo:baidu'
    keystr = '5869'
    data = {'params': 'eyJzY3JhcHlfc3ViX3Rhc2tfaWQiOiAiNjY4NzkyYTUzZGNkMWI5NDIwMDU1MjdlIiwgInNjcmFweV90YXNrX2lkIjogIjY2ODc5MmE1M2RjZDFiOTQyMDA1NTI3ZCIsICJzaWduIjogImQxMWFhZjY2NDFlOGYyYzk3YTIxM2I0YTFjYTIwNDFiIiwgInByb2plY3QiOiAiYWR2ZXJ0aXNpbmciLCAic3BpZGVyIjogInNlYXJjaCJ9', 'settings': {}, '_job': '155c5781555011ef8e0808bfb89d1deb', 'name': 'baidu'}

    res = test_queue.put(z_keys, keystr, data)
    # res = test_queue.list(z_keys)
    # res = test_queue.pop(z_keys)
    # res = test_queue.remove(z_keys, keystr)
    # res = test_queue.count(z_keys)

    print(res)
