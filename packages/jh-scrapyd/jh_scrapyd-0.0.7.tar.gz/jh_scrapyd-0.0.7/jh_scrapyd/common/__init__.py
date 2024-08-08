from jh_scrapyd.common.jh_queue import RedisQueue
import redis


# Get queue object
def get_queue(storage: redis, table: str = 'default_queue') -> RedisQueue:
    return RedisQueue(storage, table)


def get_spider_queues(config, table: str = 'spider_queue') -> RedisQueue:
    """Return a dict of Spider Queues keyed by project name"""
    section = config.SECTION
    # 获取redis配置
    config.SECTION = 'redis'
    redis_obj = redis.StrictRedis(
        host=config.get('host', 'localhost'),
        port=config.getint('port', 6379),
        db=config.getint('db', 0)
    )
    # 队列对象
    queue = get_queue(redis_obj, table)
    # 恢复
    config.SECTION = section

    return queue