from flask import request, session, url_for, render_template, json
from dao.DBServer import get_connect


def select_check():
    sql = "select id, check_object, app_id, app_name, check_enable, check_logic, check_result, check_sql from t_check"
    conn = get_connect()
    data = conn.query(sql)
    return data


def add_check():
    check_object = request.form.get('check_object')
    app_id = request.form.get('app_id')
    app_name = request.form.get('app_name')
    check_logic = request.form.get('check_logic')
    check_result = request.form.get('check_result')
    check_sql = request.form.get('check_sql')
    sql = "insert into t_check (check_object, app_id, app_name, check_enable, check_logic, check_result, check_sql) values " \
          f"(\'{check_object}\',\' {app_id}\', \'{app_name}\', '1', \'{check_logic}\', \'{check_result}\', \'{check_sql}\')"
    conn = get_connect()
    conn.execute(sql)
    return


def update_check():
    appcheackid = request.form.get('appcheackid')
    check_object = request.form.get('check_object')
    app_id = request.form.get('app_id')
    app_name = request.form.get('app_name')
    check_logic = request.form.get('check_logic')
    check_result = request.form.get('check_result')
    check_sql = request.form.get('check_sql')
    sql = f"update t_check set check_object = \'{check_object}\', app_id = \'{app_id}\', app_name = \'{app_name}\', check_logic = \'{check_logic}\', check_result = \'{check_result}\', check_sql = \'{check_sql}\' where id = \'{appcheackid}\'"
    conn = get_connect()
    conn.execute(sql)
    return


if __name__ == '__main__':
    data = ['1', '检查订单数量', '1', '会员主题', '检查订单是否小于0 ，小于0的订单不应被同步', '若行数为 0则正常，否则认为异常', 'select * from order where amount<0 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1 and 1=1']
    # select_check()
    # update_check(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
    data = select_check()
    print(data)