from zope.interface import implementer
from scrapyd.interfaces import ISpiderScheduler
from jh_scrapyd import debug_log
from jh_scrapyd.common import get_spider_queues
from jh_scrapyd.spiderqueue import JsonRedisPriorityQueue


@implementer(ISpiderScheduler)
class SpiderScheduler(object):

    def __init__(self, config):
        self.queues = None
        self.config = config
        self.update_projects()

    def schedule(self, project, spider_name, priority=0.0, **spider_args):
        # priority passed as kw for compat w/ custom queue. TODO use pos in 1.4
        # 调试日志
        debug_log('params:', spider_args, title='接口schedule方法调度')

        # 初始化队列
        queue = JsonRedisPriorityQueue(self.config, project)
        # 写入数据
        queue.add(spider_name, priority, **spider_args)


    def list_projects(self):
        # 调试日志
        debug_log(title='list_projects')
        return []

    def update_projects(self):
        self.queues = get_spider_queues(self.config)
