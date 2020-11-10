from dao.DBServer import *
from domain.topic import *


def pandect():
    app_id_list = get_connect().query("select id from t_table_base t1 where t1.table_lab ='app'")
    print(app_id_list)
    return topic('app_order_item','app_order_item','2020-11-10 15:00:00','ok-circle','remove-circle','ok-circle','ok-circle','会员销售主题')





if __name__ == '__main__':
    pandect()
