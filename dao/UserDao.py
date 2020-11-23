from dao.DBServer import get_connect


# 根据用户名，密码查询信息
def selUserBycodePwd(log_pwd):
    conn = get_connect()
    sql = "select id,username,usercode,lastupdate from t_user where usercode = \""+ log_pwd.user_code+"\" and password = \""+log_pwd.password+"\""
    row = conn.query(sql)
    return row


# 根据id,密码查询信息
def selUserById(log_id_pwd):
    conn = get_connect()
    sql = f'select id,username,usercode,lastupdate from t_user where id = \'{log_id_pwd.user_id}\' and password = \'{log_id_pwd.password}\''
    userlist = conn.query(sql)
    return userlist


# 添加登录账号信息
def insUserInfo(log_info):
    conn = get_connect()
    sql = f'INSERT INTO t_user (username,usercode,password,lastupdate) VALUES' \
          f' (\'{log_info.user_name}\',\'{log_info.user_code}\',\'{log_info.password}\',\'{log_info.nowtime}\')'
    conn.execute(sql)
    return True


# 修改密码
def updUserById(log_id_pwd):
    conn = get_connect()
    sql = f'update t_user set password = \'{log_id_pwd.password}\' where id =\'{log_id_pwd.user_id}\''
    conn.execute(sql)
    return True