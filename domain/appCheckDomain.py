class AppCheckEntity:
    def __init__(self, id, check_object, app_id, app_name, check_used, check_logic, check_result, check_sql):
        self.id = id
        self.check_object = check_object
        self.app_id = app_id
        self.app_name = app_name
        self.check_used = ord(check_used)
        self.check_logic = check_logic
        self.check_result = check_result
        self.check_sql = check_sql


class AppCheckBean:
    def __init__(self, app_id, app_name, checkdetaillist):
        self.app_id = app_id
        self.app_name = app_name
        self.checkdetaillist = checkdetaillist


class AppCheckDetailBean:
    def __init__(self, id, check_object, app_id, app_name, check_used, check_logic, check_result, check_sql):
        self.id = id
        self.check_object = check_object
        self.app_id = app_id
        self.app_name = app_name
        self.check_used = ord(check_used)
        self.check_logic = check_logic
        self.check_result = check_result
        self.check_sql = check_sql


class AppCheckInsBean:
    def __init__(self, check_object, app_id, check_used, check_logic, check_result, check_sql):
        self.check_object = check_object
        self.app_id = app_id
        self.check_used = check_used
        self.check_logic = check_logic
        self.check_result = check_result
        self.check_sql = check_sql


class AppCheckUpdBean:
    def __init__(self, appcheackid, check_object, app_id, check_used, check_logic, check_result, check_sql):
        self.id = appcheackid
        self.check_object = check_object
        self.app_id = app_id
        self.check_used = check_used
        self.check_logic = check_logic
        self.check_result = check_result
        self.check_sql = check_sql


class AppIdNameBean:
    def __init__(self, app_id, app_name):
        self.app_id = app_id
        self.app_name = app_name
