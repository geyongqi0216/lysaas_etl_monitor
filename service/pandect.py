from dao.DBServer import *
from domain.topic import *


def pandect():
    # app_id_list = get_connect().query("select id from t_table_base t1 where t1.table_lab ='app'")
    # print(app_id_list)
    data=Topic('app_order_item', 'app_order_item', '2020-11-10 15:00:00', 'ok-circle', 'remove-circle', 'ok-circle', 'ok-circle', '会员销售主题')
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