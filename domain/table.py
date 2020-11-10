# 模块 datasync 页面 table
class table:
    def __init__(self, tableid,tablecode,tablename,remark,syncstats,synctime,syncappend,synccondition,topiclist):
        self.tableid = tableid,
        self.tablecode = tablecode,
        self.tablename = tablename,
        self.remark = remark,
        self.syncstats = syncstats,
        self.synctime = synctime,
        self.syncappend = syncappend,
        self.synccondition = synccondition,
        self.topiclist = topiclist

class topic:
    def __init__(self,tableid,tablecode,tablename):
        self.tableid=tableid,
        self.tablecode=tablecode,
        self.tablename=tablename