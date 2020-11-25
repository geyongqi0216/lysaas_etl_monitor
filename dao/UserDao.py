from dao.DBServer import get_connect


# 根据用户编码，密码查询信息
def selUserByCodePsw(userloginbean):
    conn = get_connect()
    print(userloginbean.password)
    sql = f"select id, username, usercode, password, lastupdate from t_user where" \
          f" usercode = \'{userloginbean.user_code}\' and password = \'{userloginbean.password}\'"
    row = conn.query(sql)
    return row


# 根据用户编码查询信息
def selUserByCode(userinfobean):
    conn = get_connect()
    sql = "select id, username, usercode, lastupdate from t_user where usercode = \""+ userinfobean.user_code+"\""
    row = conn.query(sql)
    return row


# 添加用户登录账号信息
def insUserInfo(userinfobean):
    conn = get_connect()
    sql = f'INSERT INTO t_user (username,usercode,password,lastupdate) VALUES' \
          f' (\'{userinfobean.user_name}\',\'{userinfobean.user_code}\',\'{userinfobean.password}\'' \
          f',\'{userinfobean.nowtime}\')'
    result = conn.execute(sql)
    return result


# 修改密码
def updPswById(userupdbean):
    conn = get_connect()
    sql = f'update t_user set lastupdate = \'{userupdbean.lastupdate}\' password = \'{userupdbean.password}\' ' \
          f'where id =\'{userupdbean.user_id}\''
    result = conn.execute(sql)
    return result


# 根据id,密码查询信息
def selUserByIdPsw(userupdbean):
    sql = f'select id,username,usercode,lastupdate from t_user where id = \'{userupdbean.user_id}\' and ' \
          f'password = \'{userupdbean.old_password}\''
    conn = get_connect()
    row = conn.query(sql)
    return row
