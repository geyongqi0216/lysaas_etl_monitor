# 模块 datasync 页面 topic
class topic:
    def __init__(self, topicname , topictable, topictime, dataget, datahandle, datavalidate, datawrit, datarelation):
        self.topicname = topicname,
        self.toptable = topictable,
        self.topictime = topictime,
        self.dataget = dataget,
        self.datahandle = datahandle,
        self.datavalidate = datavalidate,
        self.datawrit = datawrit,
        self.datarelation = datarelation

class datarelation:
    def __init__(self,fronttableid,fronttablecode,fronttablename,behindtableid,behindtablecode,behindtablename):
        self.fronttableid=fronttableid,
        self.fronttablecode=fronttablecode,
        self.fronttablename=fronttablename,
        self.behindtableid=behindtableid,
        self.behindtablecode=behindtablecode,
        self.behindtablename=behindtablename