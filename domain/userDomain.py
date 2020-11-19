
class User:
    def __init__(self, id, username, usercode, password, lastupdate, effective):
        self.id = id
        self.username = username
        self.usercode = usercode
        self.password = password
        self.lastupdate = lastupdate
        self.effective = effective



    def to_string(self):
        s = "{id:{}, username:{}, usercode: {}, password:{}, lastupdate:{}}".format(
            self.id, self.username,  self.usercode, self.password, self.lastupdate)
        return s
