from jh_scrapyd.common.jh_queue import RedisQueue
import redis

# debugging mode
IS_DEBUG = False


# Whether it is debugging mode
def is_debug() -> bool:
    return IS_DEBUG


def debug_log(*kwargs, title='start'):
    if is_debug():
        print('=' * 60, title, '=' * 60)
        print(*kwargs)
        # print('=' * 60, 'end', '=' * 60)
        print("\n")


# Get queue object
def get_queue(storage: redis, table: str = 'default_queue') -> RedisQueue:
    return RedisQueue(storage, table)
