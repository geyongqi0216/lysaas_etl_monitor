
class UserInfoEntity:
    def __init__(self, id, user_name, user_code, password, lastupdate):
        self.id = id
        self.user_name = user_name
        self.user_code = user_code
        self.password = password
        self.lastupdate = lastupdate


class UserLoginBean:
    def __init__(self, user_code, password):
        self.user_code = user_code
        self.password = password


class UserInfoBean:
    def __init__(self, user_name, user_code, password, lastupdate):
        self.user_name = user_name
        self.user_code = user_code
        self.password = password
        self.lastupdate = lastupdate


class PswUpdBean:
    def __init__(self, user_id, old_password, new_password, new_password2, lastupdate):
        self.user_id = user_id
        self.old_password = old_password
        self.new_password = new_password
        self.new_password2 = new_password2
        self.lastupdate = lastupdate
