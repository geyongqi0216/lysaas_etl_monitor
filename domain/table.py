# 模块 datasync 页面 table
class table:
    def __init__(self, sourcetablename,tableid,targettablename,tablename,remark,syncstats,synctime,syncappend,synccondition,topicnamelist):
        self.sourcetablename = sourcetablename,
        self.tableid = tableid,
        self.targettablename = targettablename,
        self.tablename = tablename,
        self.remark = remark,
        self.syncstats = syncstats,
        self.synctime = synctime,
        self.syncappend = syncappend,
        self.synccondition = synccondition,
        self.topiclist = topicnamelist
