from dao.DBServer import *


def pandect():
    # 处理第一个页面的逻辑
    date = get_connect().query('select * from t_job')
    print(date)
    # 读取第一个页面需要的数据 封装成对象数组



if __name__ == '__main__':
    pandect()
