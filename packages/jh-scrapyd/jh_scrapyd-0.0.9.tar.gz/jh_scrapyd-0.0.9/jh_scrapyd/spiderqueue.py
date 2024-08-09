from jh_scrapyd.common import get_spider_queues
from jh_scrapyd import debug_log


class JsonRedisPriorityQueue(object):

    def __init__(self, config, project, table='default'):
        # 队列对象
        self.queue = get_spider_queues(config)
        self.project = project

    def add(self, name, priority=0.0, **spider_args):
        d = spider_args.copy()
        d['name'] = name
        self.put(d, priority)

    def put(self, message, priority):
        # 调试日志
        debug_log(message, title='队列put方法调度')

        return self.queue.put(self.project, message['_job'], message, float(priority))

    def pop(self):
        # 调试日志
        debug_log('project:', self.project, title='队列pop方法调度')

        return self.queue.pop(self.project)

    def count(self):
        # 个数
        c = self.queue.count(self.project)
        # 调试日志
        debug_log('count:', c, title='队列count方法调度')

        return c

    def list(self):
        # 调试日志
        debug_log('project:', self.project, title='队列list方法调度')

        return self.queue.list(self.project)

    def remove(self, func):
        # 调试日志
        debug_log('project:', self.project, title='队列remove方法调度')

    def clear(self):
        # 调试日志
        debug_log('project:', self.project, title='队列clear方法调度')

        self.queue.clear(self.project)
