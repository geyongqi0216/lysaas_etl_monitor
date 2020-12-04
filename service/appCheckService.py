from enum import Enum
from flask import request

from dao.DBServer import get_connect
from domain.appCheckDomain import AppCheckDetailBean, AppCheckBean


def editAppCheck():
    class ReturnInfo(Enum):
        addSuc = "成功创建规则,点击返回"
        addFai = "规则创建失败,点击返回"
        editSuc = "成功更新规则,点击返回"
        editFai = "规则更新失败,点击返回"

    app_check_id = request.form.get('appcheck_id')
    app_id_r = request.form.get('app_id')
    app_id = 0 if app_id_r is None else app_id_r
    check_object = request.form.get('check_object')
    check_used = request.form.get('check_used')
    check_logic = request.form.get('check_logic')
    check_result = request.form.get('check_result')
    check_sql = request.form.get('check_sql')
    # 判断是否为新增
    if app_check_id == '0':
        sql = "insert into t_check (app_id, check_object, check_used, check_logic, check_result, check_sql) values ( '" \
              + app_id + "' , %s , " + check_used + " , %s , %s , %s ); "
    else:
        sql = "update t_check set check_object = %s, check_used = " + check_used + ", check_logic = %s, check_result = %s," \
            " check_sql = %s where id =  " + app_check_id + " ;"
    conn = get_connect()
    args = [check_object,check_logic,check_result,check_sql]
    result = conn.execute(sql,args)
    if app_check_id != '0' and result is not None and result > 0:
        return "<a href='datasyncappcheck' >"+ReturnInfo.editSuc.value+"</a>"
    elif app_check_id != '0':
        return "<a href='datasyncappcheck' >"+ReturnInfo.editFai.value+"</a>"
    elif app_check_id == '0' and result is not None and result > 0:
        return "<a href='datasyncappcheck' >"+ReturnInfo.addSuc.value+"</a>"
    elif app_check_id == '0':
        return "<a href='datasyncappcheck' >"+ReturnInfo.addFai.value+"</a>"


def getAppCheckList():
    app_check_list = []
    conn = get_connect()
    # 查询所有主题信息
    sql = "select distinct c.app_id, t.table_name from t_check c left join t_table_base t on c.app_id =t.id"
    check_app_list = conn.query(sql)
    # 循环所有主题信息
    for each_check_app in check_app_list:
        # 根据主题信息查询t_app_check所有详情信息
        sql = f"select c.id, c.check_object, c.app_id, t.table_name, c.check_used, c.check_logic, c.check_result, c.check_sql from t_check c left join t_table_base t on c.app_id =t.id " \
              f" and t.table_lab = 'topic' where app_id = '"+str(each_check_app[0])+"'"
        check_list = conn.query(sql)
        app_check_detail_list = []
        for each_check in check_list:
            app_check_detail = AppCheckDetailBean(each_check[0], each_check[1], each_check[2], each_check[3], each_check[4], each_check[5], each_check[6], each_check[7])
            app_check_detail_list.append(app_check_detail)
        # 将主题信息和相对的详情信息打包成对象
        app_check = AppCheckBean(each_check_app[0], each_check_app[1], app_check_detail_list)
        # 传进最后appchecklist中
        app_check_list.append(app_check)
    return app_check_list




def getTopicList():
    app_check_list = []
    conn = get_connect()
    # 查询所有主题信息
    sql = "select t.id, t.table_name from t_table_base t where t.table_lab = 'topic' "
    topic_list = conn.query(sql)
    return topic_list
