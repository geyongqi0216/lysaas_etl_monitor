from enum import Enum


class UserInfoEntity:
    def __init__(self, id, user_name, user_code, password, last_update, effective):
        self.id = id
        self.user_name = user_name
        self.user_code = user_code
        self.password = password
        self.last_update = last_update
        self.effective = effective


class UserCodePwdBean:
    def __init__(self, user_code, password):
        self.user_code = user_code
        self.password = password


class UserLogInfoBean:
    def __init__(self, user_name, user_code, password, nowtime):
        self.user_name = user_name
        self.user_code = user_code
        self.password = password
        self.now_Time = nowtime


class UserIdPwd:
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password


class Error(Enum):
    id_pwd_error = '用户名或密码错误'
    pwd_finish = '密码修改完成'
    oldpwd_error = '原始密码错误'
    oldpwd_newpwd_error = '两次密码不一致'
    upd_error = '修改有误'