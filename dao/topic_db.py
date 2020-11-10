from dao.DBServer import *

def aa():
    #
    get_connect().gen_query('select * from t_log_daily_view')
