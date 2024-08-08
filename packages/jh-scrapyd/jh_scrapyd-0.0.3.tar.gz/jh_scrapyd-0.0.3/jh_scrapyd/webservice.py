import traceback
from twisted.python import log
from scrapyd.utils import JsonResource
from copy import copy
import uuid
from scrapyd.config import Config
from scrapyd.utils import get_spider_list, native_stringify_dict
from jh_scrapyd.scheduler import SpiderScheduler


class WsResource(JsonResource):

    def __init__(self, root):
        JsonResource.__init__(self)
        self.root = root

    def render(self, txrequest):
        try:
            return JsonResource.render(self, txrequest).encode('utf-8')
        except Exception as e:
            if self.root.debug:
                return traceback.format_exc().encode('utf-8')
            log.err()
            r = {"node_name": self.root.nodename, "status": "error", "message": str(e)}
            return self.render_object(r, txrequest).encode('utf-8')


class JhSchedule(WsResource):

    def render_POST(self, txrequest):
        args = native_stringify_dict(copy(txrequest.args), keys_only=False)
        settings = args.pop('setting', [])
        settings = dict(x.split('=', 1) for x in settings)
        args = {k: v[0] for k, v in args.items()}
        project = args.pop('project')
        spider = args.pop('spider')
        version = args.get('_version', '')
        priority = float(args.pop('priority', 0))
        spiders = get_spider_list(project, version=version)
        if spider not in spiders:
            return {"status": "error", "message": "spider '%s' not found" % spider}
        args['settings'] = settings
        jobid = args.pop('jobid', uuid.uuid1().hex)
        args['_job'] = jobid

        # self.root.scheduler.schedule(project, spider, priority=priority, **args)

        # 投入队列
        config = Config()
        scheduler = SpiderScheduler(config)
        scheduler.schedule(project, spider, priority, **args)

        return {"node_name": self.root.nodename, "status": "ok", "jobid": jobid}


class JhCancel(WsResource):
    #  {'project': 'demo', 'job': '8eca9e8f549211ef8f7e08bfb89d1deb'}
    def render_POST(self, txrequest):
        args = {k: v[0] for k, v in native_stringify_dict(copy(txrequest.args), keys_only=False).items()}
        project = args['project']
        jobid = args['job']
        signal = args.get('signal', 'TERM')

        # 删除running
        _is_ok = self._rm_by_running(project, jobid, signal)

        prevstate = None
        if _is_ok:
            prevstate = 'running'
        else:
            _is_ok = self._rm_by_pending(project, jobid)
            if _is_ok:
                prevstate = 'pending'

        return {"node_name": self.root.nodename, "status": "ok" if _is_ok else "error", "prevstate": prevstate}

    def _rm_by_running(self, project, jobid, signal) -> bool:
        _is = False
        spiders = self.root.launcher.processes.values()
        for s in spiders:
            if s.project == project and s.job == jobid:
                s.transport.signalProcess(signal)
                _is = True
        return _is

    def _rm_by_pending(self, project, jobid) -> bool:
        # 创建调度对象
        config = Config()
        scheduler = SpiderScheduler(config)

        return scheduler.cancel(project, jobid)
