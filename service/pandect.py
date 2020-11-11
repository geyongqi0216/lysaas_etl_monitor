from dao.DBServer import *
from domain.datasyncBean import *


def pandect_topic():
    data = []
    dataget = Stepstats('SUC', '', '')
    datahandle = Stepstats('WAR', '数据缺失', 'wx_order微信订单 - 数据更新异常,pos_order线下订单 - 数据更新异常')
    datavalidate = Stepstats('FAI', '处理失败', '数据缺失')
    datawrit = Stepstats('STOP', '未执行', '此节点未执行')
    datarelationlist = [Datarelation('', 'wx_order', '微信订单', '', '', ''),
                        Datarelation('', 'pos_order', '线下订单', '', '', ''),
                        Datarelation('', 'tm_order', '淘宝订单', '', '', '')]
    data.append(Topic('app_order_item', 'app_order_item', '2020-11-10 15:00:00', dataget, datahandle, datavalidate, datawrit, datarelationlist))
    return data


def pandect_table():
    data = []
    datarelationlist = [Datarelation('', '', '', '', 'app_order', '订单主题'),
                        Datarelation('', '', '', '', 'app_member', '会员主题'   ),
                        Datarelation('', '', '', '', 'app_guide', '导购主题')]
    data.append(Table('crm_shop', '1', 'src_shop', '店铺信息', '全渠道店铺基础信息', 'SUC', '2020-01-01 15:37', '1', '2020-01-01~2020-01-07', datarelationlist))
    return data


if __name__ == '__main__':
    # data = pandect()
    # print(data.topicname, data.datawrit)
    # if data.topicname[0] == '123':
    #     print(True)
    # else:
    #     print(False)
    # test()
    print(Topic1('123').topicname)
