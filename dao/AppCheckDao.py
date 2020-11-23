from dao.DBServer import get_connect


# 根据用户名，密码查询信息
def selCheckByAppid(app_id):
    conn = get_connect()
    sql = f"select t1.id, t1.check_object, t1.app_id , t2.table_name, t1.check_used, t1.check_logic, t1.check_result, t1.check_sql " \
                "from t_check as t1 " \
           "inner join t_table_base as t2  " \
                "on t1.app_id = t2.id  " \
          f"where t2.table_lab = 'topic' and t1.app_id =\'{app_id}\'"
    rows = conn.query(sql)
    return rows


# 查看关联的主题id，主题名称
def selCheckAppid():
    conn = get_connect()
    sql = '''
            select distinct t1.app_id , t2.table_name 
                from t_check as t1
            inner join t_table_base as t2  
                on t1.app_id = t2.id  
            where t2.table_lab = 'topic'
           '''
    rows = conn.query(sql)
    return rows


# 添加check信息
def insCheckInfo(check_info):
    conn = get_connect()
    sql = "insert into t_check (check_object, app_id, check_used, check_logic, check_result, check_sql) values " \
          f"(\'{check_info.check_object}\',\' {check_info.app_id}\', '1'" \
          f", \'{check_info.check_logic}\', \'{check_info.check_result}\', \'{check_info.check_sql}\')"
    conn.execute(sql)
    return


# 编辑信息
def updCheckById(check_info):
    conn = get_connect()
    sql = f"update t_check set check_object = \'{check_info.check_object}\', app_id = \'{check_info.app_id}\'" \
          f", check_logic = \'{check_info.check_logic}\', check_result = \'{check_info.check_result}\'" \
          f", check_sql = \'{check_info.check_sql}\' where id = \'{check_info.appcheackid}\'"
    conn.execute(sql)
    return True