class appCheckEntity():
    def __init__(self, appcheackid, app_id, check_object, check_logic, check_result, check_sql):
        self.appcheackid = appcheackid
        self.app_id = app_id
        self.check_object = check_object
        self.check_logic = check_logic
        self.check_result = check_result
        self.check_sql = check_sql

    def to_string(self):
        s = "{appcheackid:{}, app_id:{}, check_object: {}, check_logic:{}, check_result:{}, check_sql:{}}".format(
            self.appcheackid, self.app_id,  self.check_object, self.check_logic, self.check_result, self.check_sql)
        return s


class appCheckBean():
    def __init__(self, app_id, app_name, appchecklist):
        self.app_id = app_id
        self.app_name = app_name
        self.appchecklist = appchecklist


class appCheckDetailBean():
    def __init__(self, app_id, appcheackid, check_enable, check_object, check_logic, check_result, check_sql):
        self.app_id = app_id
        self.appcheackid = appcheackid
        self.check_used = check_enable
        self.check_object = check_object
        self.check_logic = check_logic
        self.check_result = check_result
        self.check_sql = check_sql

