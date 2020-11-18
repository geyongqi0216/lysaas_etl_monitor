
class User:
    def __init__(self, row):
        self.id = row[0]
        self.username = row[1]
        self.usercode = row[2]
        self.password = row[3]
        self.lastupdate = row[4]

    def to_string(self):
        s = "{id:{}, username:{}, usercode: {}, password:{}, lastupdate:{}}".format(
            self.id, self.username,  self.usercode, self.password, self.lastupdate)
        return s
