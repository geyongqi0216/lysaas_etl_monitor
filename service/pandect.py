from dao.DBServer import *
from domain.topic import *


def pandect():
    # app_id_list = get_connect().query("select id from t_table_base t1 where t1.table_lab ='app'")
    # print(app_id_list)
    dataget = Stepstats('SUC', '', '')
    datahandle = Stepstats('WAR', '渠道数据缺失', 'wx_order微信订单 - 数据更新异常')
    datavalidate = Stepstats('FAI', '处理失败', '数据缺失')
    datawrit = Stepstats('STOP', '未执行', '此节点未执行')
    datarelationlist = [Datarelation('', 'wx_order', '微信订单', '', '', ''),
                        Datarelation('', 'pos_order', '线下订单', '', '', ''),
                        Datarelation('', 'tm_order', '淘宝订单', '', '', '')]
    data=Topic('app_order_item', 'app_order_item', '2020-11-10 15:00:00', dataget, datahandle, datavalidate, datawrit, datarelationlist)
    # print(data.topicname,'')
    return data


class Foo:
    def __init__(self, a='123'):
        self.a=a

def test():
    f=Foo()
    print(f.a)

if __name__ == '__main__':
    # data = pandect()
    # print(data.topicname, data.datawrit)
    # if data.topicname[0] == '123':
    #     print(True)
    # else:
    #     print(False)
    # test()
    print(Topic1('123').topicname)