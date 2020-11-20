from flask import request, session, url_for, render_template, json
from dao.DBServer import get_connect
from domain.appcheckBean import appCheckEntity, appCheckBean, appCheckDetailBean


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


def get_check():
    appchecklist = []
    conn = get_connect()
    # 查询所有主题信息
    sql = "select distinct app_id, app_name from t_check"
    app_list = conn.query(sql)
    # 循环所有主题信息
    for app_each in app_list:
        # 根据主题信息查询t_check所有详情信息
        sql = f"select id, check_object, app_id, app_name, check_enable, check_logic, check_result, check_sql from t_check where app_id = \'{app_each[0]}\' and app_name =\'{app_each[1]}\'"
        checkList = conn.query(sql)
        appCheckDetaillist = []
        for check in checkList:
            appCheckDetail = appCheckDetailBean(check[0], check[1], check[2], check[3], check[4], check[5], check[6], check[7])
            appCheckDetaillist.append(appCheckDetail)
        # 将主题信息和相对的详情信息打包成对象
        appcheck = appCheckBean(app_each[0], app_each[1], appCheckDetaillist)
        # 传进最后appchecklist中
        appchecklist.append(appcheck)
    return appchecklist


if __name__ == '__main__':
    appchecklist = get_check()
    for appcheck in appchecklist:
        print(appcheck.app_id,appcheck.app_name,appcheck.checkdetaillist)
