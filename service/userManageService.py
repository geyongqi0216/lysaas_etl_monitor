import datetime
from flask import request, session, url_for, render_template, json
from werkzeug.utils import redirect
from dao.UserDao import selUserBycodePwd, insUserInfo, selUserById, updUserById
from domain.userDomain import UserCodePwdBean, UserLogInfoBean, UserIdPwd, Error


# 查询user信息
def doLogin():
    # 从前端中获取登录信息
    user_code = request.form.get('userCode')  # 获取用户编码
    password = request.form.get('userPwd')  # 获取用户密码
    log_pwd = UserCodePwdBean(user_code, password)
    # 根据userCode，userPwd查询数据
    userlist = selUserBycodePwd(log_pwd)
    # 判断若有数据，登录成功
    if userlist is not None and len(userlist) > 0:
        session['user.id'] = str(userlist[0][0])
        session['user.username'] = str(userlist[0][1])
        session['user.usercode'] = str(userlist[0][2])
        session['user.effective'] = (datetime.datetime.now() + datetime.timedelta(minutes=int(30))).strftime("%Y-%m-%d %H:%M:%S")
        return redirect(url_for('index'))
    return render_template('login.html', errorInfo=Error.id_pwd_error)  # errorInfo对应页面参数errorInfo


# 添加user登录信息
def addUserLogin():
    # 从前端中获取注册信息
    user_name = request.form.get('userName')  # 获取用户名称
    user_code = request.form.get('userCode')     # 获取用户编码
    password = request.form.get('userPwd')  # 获取用户密码
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_pwd = UserCodePwdBean(user_code, password)
    log_info = UserLogInfoBean(user_name, user_code, password, nowtime)
    # 查询是否有相同此用户
    row = selUserBycodePwd(log_pwd)
    # 判断若没有相同用户信息，添加成功
    if len(row) > 0:
        return render_template('register.html')
    else:
        result = insUserInfo(log_info)
        if result:
            return render_template('register_ok.html')
        else:
            return render_template('register.html')


# 修改user密码
def editUserPwd():
    # 从前端中获取用户修改密码信息
    user_id = session.get("user.id")
    old_password = request.form.get('passwordForm-oldpsd')  # 获取键入的旧密码
    new_password = request.form.get('passwordForm-newpsd')  # 获取键入的新密码
    new_password2 = request.form.get('passwordForm-repsd')
    log_id_old_pwd = UserIdPwd(user_id, old_password)
    # 判断两次新密码是否一致
    if new_password == new_password2:
        # 找出是否有该用户，进行核对
        userlist = selUserById(log_id_old_pwd)
        # 两次输入密码一致且有此用户，修改成功
        if len(userlist) > 0:
            log_id_new_pwd = UserIdPwd(user_id, new_password)
            result = updUserById(log_id_new_pwd)
            if result:
                return json.dumps(Error.pwd_finish, ensure_ascii=False)
            else:
                return json.dumps(Error.upd_error, ensure_ascii=False)
        return json.dumps(Error.oldpwd_error, ensure_ascii=False)
    return json.dumps(Error.oldpwd_newpwd_error, ensure_ascii=False)
