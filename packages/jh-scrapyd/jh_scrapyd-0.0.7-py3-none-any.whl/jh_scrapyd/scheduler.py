from zope.interface import implementer

from scrapyd.interfaces import ISpiderScheduler
from jh_scrapyd import debug_log
from jh_scrapyd.common import get_spider_queues


@implementer(ISpiderScheduler)
class SpiderScheduler(object):

    def __init__(self, config):
        self.queues = None
        self.config = config
        self.update_projects()

    def schedule(self, project, spider_name, priority=0.0, **spider_args):
        # priority passed as kw for compat w/ custom queue. TODO use pos in 1.4
        # 赋值
        params = spider_args.copy()
        params['name'] = spider_name

        # 调试日志
        debug_log('params:', params, title='接口schedule方法调度')

        # 写入数据
        self.queues.put(project, params['_job'], params, priority)

    def cancel(self, project, jobid):
        # Delete queue data

        # 调试日志
        debug_log('project:', project,jobid, title='接口cancel方法调度')

        return self.queues.remove(project, jobid)

    def list_projects(self):
        # 调试日志
        debug_log(title='list_projects')
        return []

    def update_projects(self):
        self.queues = get_spider_queues(self.config)
