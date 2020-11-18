# 登录
import datetime
from flask import request, session, url_for, render_template
from werkzeug.utils import redirect
from dao.DBServer import get_connect


def get_login():
    usercode = request.form.get('userCode')  # 从表单中获取数据
    password = request.form.get('userPwd')
    conn = get_connect()
    sql = "select id,username,usercode,lastupdate from t_user where usercode = \""+usercode+"\" and password = \""+password+"\""
    rows = conn.query(sql)
    if rows is not None and len(rows) > 0:
        session['user.id'] = str(rows[0][0])
        session['user.username'] = str(rows[0][1])
        session['user.usercode'] = str(rows[0][2])
        session['user.lastupdate'] = str(rows[0][3])
        session['user.effective'] = (datetime.time.datetime.now() + datetime.timedelta(minutes=int(30))).strftime("%Y-%m-%d %H:%M:%S")

        return redirect(url_for('index'))
    return render_template('login.html', errorInfo='用户名或密码错误')  # errorInfo对应页面参数errorInfo


# 注册
def get_register():
    conn = get_connect()
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')  # 从表单中获取数据
        usercode = request.form.get('usercode')
        password = request.form.get('password')
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = f'select id,username,usercode,password,lastupdate from t_user where username = \'{username}\''
        data = conn.query(sql)
        if len(data) > 0:
            return render_template('register.html', error='用户名已存在')
        else:
            sql = f'INSERT INTO t_user (username,usercode,password,lastupdate) VALUES (\'{username}\',\'{usercode}\',\'{password}\',\'{nowTime}\')'
            conn.query(sql)
            return render_template('register_ok.html')

# 修改
def get_update():
    # 传进来三个密码一个用户名
    # 密码是否一致  是：继续
    #
    # 查找数据库有没有这个人，密码 是：继续
    # 进行修稿
    username = request.form.get('username')  # 从表单中获取数据
    old_password = request.form.get('old_password')
    new_password = request.form.get('new_password')
    new_password2 = request.form.get('new_password2')
    if new_password == new_password2:
        sql = f'select id,username,usercode,password,lastupdate from t_user where username = \'{username}\' and password = \'{old_password}\''
        conn = get_connect()
        data = conn.query(sql)
        if len(data) > 0:
            if data[0][1] == username and data[0][3] == old_password:
                id = data[0][0]
                sql = f'update t_user password = \'{new_password}\' where id =\'{id}\''
                conn.execute(sql)
                return
    return