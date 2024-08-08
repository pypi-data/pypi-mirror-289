from abc import ABC, abstractmethod
import time
import redis
import logging


def _str_decode(b):
    if isinstance(b, bytes):
        return b.decode('utf-8', errors='ignore')
    else:
        return str(b)


def _gen_key(arr, sep: str = ':') -> str:
    return sep.join([_str_decode(s) for s in arr])


def bytes_dict_to_str_dict(input_dict):
    """
    将字典中的所有bytes类型的键和值转换为str类型。

    参数:
        input_dict (dict): 包含bytes类型键和值的字典。

    返回:
        dict: 所有键和值都转换为str类型的新字典。
    """
    # 使用字典推导式来创建新的字典，其中所有键和值都转换为字符串
    return {key.decode('utf-8') if isinstance(key, bytes) else key:
                value.decode('utf-8') if isinstance(value, bytes) else value
            for key, value in input_dict.items()}


class Queue(ABC):
    def __init__(self, storage, table='scrapyd'):
        """Initialize queue"""
        self.storage = storage
        self.table = table
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
        """
        分数权重计算
        :param score:
        :return:
        """
        return int(self.now_time * score)


class RedisQueue(Queue):
    """
    z_key：集合键，例如：set:demo
    key：分数键，例如：abc1235869
    """
    SET_NAME = 'set'
    HASH_NAME = 'hash'

    def put(self, z_key: str, key: str, data: dict, score: float = 1) -> bool:
        if not data:
            return False

        try:
            # 添加到有序集合中
            key_str = self._gen_set_key(z_key)
            self.storage.zadd(key_str, {key: self.score_weight(score)})

            # 添加到hash中
            z_key_str = self._gen_hash_key(z_key, key)
            self.storage.hset(name=z_key_str, mapping=data)
            return True
        except redis.RedisError as e:
            logging.error(f"Error adding task to queue: {e}")
            return False

    def pop(self, z_key: str, desc: bool = True):
        try:
            # 获取集合
            z_key_str = self._gen_set_key(z_key)
            res = self.storage.zrange(z_key_str, 0, 1, desc, True)
            if not res:
                return {}

            # 获取数据
            key = res[0][0]
            hash_key = self._gen_hash_key(z_key, key)
            result = self.storage.hgetall(hash_key)

            # 删除出列的数据
            self.remove(z_key, key)
            return bytes_dict_to_str_dict(result)
        except redis.RedisError as e:
            logging.error(f"Error popping task from queue: {e}")
            return {}

    def remove(self, z_key: str, key: str) -> bool:
        try:
            # 使用Redis事务确保操作的原子性
            with self.storage.pipeline() as pipe:
                z_key_str = self._gen_set_key(z_key)
                pipe.zrem(z_key_str, key)
                pipe.delete(self._gen_hash_key(z_key, key))
                pipe.execute()
            return True
        except redis.RedisError as e:
            logging.error(f"Error removing task from queue: {e}")
            return False

    def list(self, z_key: str, desc: bool = True):
        try:
            # 获取集合
            z_key_str = self._gen_set_key(z_key)
            key_list = self.storage.zrange(z_key_str, 0, -1, desc, True)

            # 结果集
            result = [
                bytes_dict_to_str_dict(self.storage.hgetall(self._gen_hash_key(z_key, item[0])))
                for item in key_list
            ]
            return result
        except redis.RedisError as e:
            logging.error(f"Error listing tasks from queue: {e}")
            return []

    def count(self, z_key: str) -> int:
        try:
            # 获取集合个数
            z_key_str = self._gen_set_key(z_key)

            return self.storage.zcard(z_key_str)
        except redis.RedisError as e:
            logging.error(f"Error obtaining the number of queues: {e}")
            return 0

    def clear(self, z_key: str):
        # 删除集合
        z_keys = self._gen_set_key(z_key)
        self._clear_by_prefix(z_keys)

        # 删除hash
        hash_key = _gen_key([self.table, self.HASH_NAME, z_key])
        self._clear_by_prefix(hash_key)

    def _clear_by_prefix(self, prefix: str) -> bool:
        try:
            # 按指定前缀删除redis数据
            cursor = 0
            pipeline = self.storage.pipeline()

            while True:
                cursor, keys = self.storage.scan(cursor=cursor, match=f"{prefix}*", count=1000)
                if keys:
                    for key in keys:
                        pipeline.delete(key)
                    pipeline.execute()
                if cursor == 0:
                    break
            return True
        except redis.RedisError as e:
            logging.error(f"Error deleting specified key: {prefix}")
            return False

    def _gen_hash_key(self, z_key, key) -> str:
        return _gen_key([self.table, self.HASH_NAME, z_key, key])

    def _gen_set_key(self, z_key) -> str:
        return _gen_key([self.table, self.SET_NAME, z_key])

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
    test_queue = RedisQueue(redis_client)

    z_keys = 'demo:baidu'
    keystr = '5869'
    # res = test_queue.put(z_keys, key, {'name': 'Mr Ye', 'age': 18})
    # res = test_queue.list(z_keys)
    # res = test_queue.pop(z_keys)
    # res = test_queue.remove(z_keys, keystr)
    res = test_queue.count(z_keys)

    print(res)
