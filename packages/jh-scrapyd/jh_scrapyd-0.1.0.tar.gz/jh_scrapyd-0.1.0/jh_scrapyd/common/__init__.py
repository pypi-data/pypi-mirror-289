from jh_scrapyd.common.jh_queue import RedisQueue
import redis


# Get queue object
def get_queue(storage: redis, table: str = 'default', is_unified_queue: bool = False) -> RedisQueue:
    return RedisQueue(storage, table, is_unified_queue)


def get_spider_queues(config) -> RedisQueue:
    """Return a dict of Spider Queues keyed by project name"""
    section = config.SECTION

    # 获取redis配置
    config.SECTION = 'jh_scrapyd'
    conf = {
        'host': config.get('host', 'localhost'),
        'port': config.getint('port', 6379),
        'db': config.getint('db', 0)
    }
    password = config.get('password')
    if password:
        conf['password'] = password
    redis_obj = redis.StrictRedis(
        **conf
    )

    # 获取是否统一队列参数
    is_unified_queue = True if config.getint('is_unified_queue') else False

    # 获取表名称
    table = config.get('queue_prefix', 'default')

    # 创建队列对象
    queue = get_queue(redis_obj, table, is_unified_queue)

    # 恢复配置分组
    config.SECTION = section

    return queue
