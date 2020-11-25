import datetime
from flask import request, session, url_for, render_template, json
from werkzeug.utils import redirect
from dao.UserDao import selUserByCode, insUserInfo, updPswById, selUserByIdPsw, selUserByCodePsw
from domain.userDomain import UserInfoBean, PswUpdBean, UserLoginBean, UserInfoEntity
from enum import Enum


class ReturnInfoEnum:
    class Login(Enum):
        id_pwd_error = '用户名或密码错误'

    class Edit(Enum):
        upd_success = '密码修改成功'
        oldpwd_error = '原始密码错误'
        oldpwd_newpwd_error = '两次密码不一致'
        upd_error = '修改有误'  # TODO 未知异常：系统异常，请联系客服！

    class Add(Enum):
        code_exist_error = '用户名已存在'
        ins_seccess = '注册成功'
        ins_error = '注册失败'  # TODO 未知异常：系统异常，请联系客服！


# 用户登录
def doLogin():
    # 从前端中获取登录信息
    user_code = request.form.get('userCode')  # 获取用户编码
    password = request.form.get('userPwd')  # 获取用户密码
    userloginbean = UserLoginBean(user_code, password)
    # 根据userCode，userPsw查询数据
    userlist = selUserByCodePsw(userloginbean)
    # 判断若有数据，登录成功
    if len(userlist) == 1:
        userinfoentity = UserInfoEntity(userlist[0][0], userlist[0][1], userlist[0][2], userlist[0][3], userlist[0][4])
        session['user.id'] = userinfoentity.id
        session['user.username'] = userinfoentity.user_name
        session['user.usercode'] = userinfoentity.user_code
        session['user.effective'] = (datetime.datetime.now()
                                     + datetime.timedelta(minutes=int(30))).strftime("%Y-%m-%d %H:%M:%S")
        return redirect(url_for('index'))
    return render_template('login.html', errorInfo=ReturnInfoEnum.Login.id_pwd_error.value)  # errorInfo对应页面参数errorInfo


# 添加user信息
def addUserInfo():
    # 从前端中获取注册信息
    user_name = request.form.get('userName')  # 获取用户名称
    user_code = request.form.get('userCode')     # 获取用户编码
    password = request.form.get('userPsw')  # 获取用户密码
    lastupdate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 目前修改时间
    userinfobean = UserInfoBean(user_name, user_code, password, lastupdate)
    # 查询是否有相同此用户
    row = selUserByCode(userinfobean)
    # 判断若有相同用户信息，返回“用户名已存在”
    if len(row) > 0:
        return render_template('register.html', errorInfo=ReturnInfoEnum.Add.code_error.value)
    else:
        # 判断是否成功
        result = insUserInfo(userinfobean)
        if result == 1:
            return render_template('register_ok.html', errorInfo=ReturnInfoEnum.Add.ins_seccess.value)
        else:
            return render_template('register.html', errorInfo=ReturnInfoEnum.Add.ins_error.value)


# 修改user密码
def editUserPsw():
    # 从前端中获取用户修改密码信息
    user_id = session.get("user.id")
    old_password = request.form.get('passwordForm-oldpsd')  # 获取键入的旧密码
    new_password = request.form.get('passwordForm-newpsd')  # 获取键入的新密码
    new_password2 = request.form.get('passwordForm-repsd')
    lastupdate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 目前修改时间
    userupdbean = PswUpdBean(user_id, old_password, new_password, new_password2, lastupdate)
    # 新密码是否为空
    # 判断两次新密码是否一致
    if userupdbean.new_password == userupdbean.new_password2:
        # 旧密码是否一致
        row = selUserByIdPsw(userupdbean)
        if len(row) == 1:
            # 插入语句是否成功
            result = updPswById(userupdbean)
            if result == 1:
                return json.dumps(ReturnInfoEnum.Edit.pwd_seccess.value, ensure_ascii=False)
            else:
                return json.dumps(ReturnInfoEnum.Edit.upd_error.value, ensure_ascii=False)
        return json.dumps(ReturnInfoEnum.Edit.oldpwd_error.value, ensure_ascii=False)
    return json.dumps(ReturnInfoEnum.Edit.oldpwd_newpwd_error.value, ensure_ascii=False)
