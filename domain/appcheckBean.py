class appCheckEntity():
    def __init__(self, id, check_object, app_id, app_name, check_enable, check_logic, check_result, check_sql):
        self.id = id
        self.check_object = check_object
        self.app_id = app_id
        self.app_name = app_name
        self.check_used = check_enable
        self.check_logic = check_logic
        self.check_result = check_result
        self.check_sql = check_sql

    def to_string(self):
        s = "{id:{}, app_id:{}, check_object: {}, check_logic:{}, check_result:{}, check_sql:{}}".format(
            self.id, self.app_id,  self.check_object, self.check_logic, self.check_result, self.check_sql)
        return s


class appCheckBean():
    def __init__(self, id, app_id, checkdetaillist):
        self.id = id
        self.app_id = app_id
        self.checkdetaillist = checkdetaillist


class appCheckDetailBean():
    def __init__(self, id, check_object, app_id, app_name, check_used, check_logic, check_result, check_sql):
        self.id = id
        self.check_object = check_object
        self.app_id = app_id
        self.app_name = app_name
        self.check_used = check_used
        self.check_logic = check_logic
        self.check_result = check_result
        self.check_sql = check_sql

