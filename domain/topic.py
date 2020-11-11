class Topic:
    def __init__(self, topicname, topictable, topictime, dataget, datahandle, datavalidate, datawrit, datarelationlist):
        self.topicname = topicname
        self.topictable = topictable
        self.topictime = topictime
        self.dataget = dataget
        self.datahandle = datahandle
        self.datavalidate = datavalidate
        self.datawrit = datawrit
        self.datarelationlist = datarelationlist


class Stepstats:
    def __init__(self, stats, title, memo):
        self.stats = stats
        self.title = title  # 弹窗标题
        self.memo = memo  # 弹窗内容


class Datarelation:
    def __init__(self, fronttableid, fronttablecode, fronttablename, behindtableid, behindtablecode, behindtablename):
        self.fronttableid = fronttableid
        self.fronttablecode = fronttablecode
        self.fronttablename = fronttablename
        self.behindtableid = behindtableid
        self.behindtablecode = behindtablecode
        self.behindtablename = behindtablename
