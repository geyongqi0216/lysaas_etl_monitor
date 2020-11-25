from dao.DBServer import get_connect


# 根据app_id查询check信息
def selCheckByAppId(appidnamebean):
    conn = get_connect()
    sql = f"select t1.id, t1.check_object, t1.app_id , t2.table_name, t1.check_used, t1.check_logic, t1.check_result, t1.check_sql " \
            "from t_check as t1 inner join t_table_base as t2 on t1.app_id = t2.id  " \
          f"where t2.table_lab = 'topic' and t1.app_id =\'{appidnamebean.app_id}\'"
    rows = conn.query(sql)
    return rows


# 查看主题id，主题名称
def selCheckApp():
    conn = get_connect()
    sql = '''
            select distinct t1.app_id , t2.table_name from t_check as t1
            inner join t_table_base as t2 on t1.app_id = t2.id where t2.table_lab = 'topic'
           '''
    rows = conn.query(sql)
    return rows


# 添加check信息
def insCheckInfo(appcheckinsbean):
    conn = get_connect()
    sql = "insert into t_check (check_object, app_id, check_used, check_logic, check_result, check_sql) values " \
          f"(\'{appcheckinsbean.check_object}\',\' {appcheckinsbean.app_id}\', \'{appcheckinsbean.check_used}\''" \
          f", \'{appcheckinsbean.check_logic}\', \'{appcheckinsbean.check_result}\', \'{appcheckinsbean.check_sql}\')"
    result = conn.execute(sql)
    return result


# 根据id修改信息
def updCheckById(appcheckupdbean):
    conn = get_connect()
    sql = f"update t_check set check_object = \'{appcheckupdbean.check_object}\', app_id = \'{appcheckupdbean.app_id}\'" \
          f", check_logic = \'{appcheckupdbean.check_logic}\', check_result = \'{appcheckupdbean.check_result}\'" \
          f", check_sql = \'{appcheckupdbean.check_sql}\', check_used = \'{appcheckupdbean.check_used}\'" \
          f" where id = \'{appcheckupdbean.appcheackid}\'"
    result = conn.execute(sql)
    return result