from dao.DBServer import get_connect
# etl_log 对象
class EtlLog:

    def __init__(self, id, t_job_id, config_id, dag_name, task_name, source_table_name, target_table_name,
                 sync_condition,
                 sync_start_time, sync_end_time, source_number, target_number, append_number, number_check, exec_state,
                 error_log, task_start_time, task_end_time, task_use_time, timestamp_v):
        self.id = id
        self.t_job_id = t_job_id
        self.config_id = config_id
        self.dag_name = dag_name
        self.task_name = task_name
        self.source_table_name = source_table_name
        self.target_table_name = target_table_name
        self.sync_condition = sync_condition
        self.sync_start_time = sync_start_time
        self.sync_end_time = sync_end_time
        self.source_number = source_number
        self.target_number = target_number
        self.append_number = append_number
        self.number_check = number_check
        self.exec_state = exec_state
        self.error_log = error_log
        self.task_start_time = task_start_time
        self.task_end_time = task_end_time
        self.task_use_time = task_use_time
        self.timestamp_v = timestamp_v

    def __str__(self):
        return (self.t_job_id, self.config_id, self.dag_name, self.task_name, self.source_table_name, \
                self.target_table_name, self.sync_condition, self.sync_start_time, self.sync_end_time, \
                self.source_number, self.target_number, self.append_number, self.number_check, self.exec_state, \
                self.error_log, self.task_start_time, self.task_end_time, self.task_use_time, self.timestamp_v)

def sendEtlLogGetId(etlLog):
    #conn = get_connect()
    sql = "INSERT INTO etlmonitor.t_job_log(t_job_id, config_id, dag_name, task_name, source_table_name, "\
                 "target_table_name, sync_condition, sync_start_time, sync_end_time, source_number, target_number, "\
                 "append_number, number_check, exec_state, error_log, task_start_time, task_end_time, task_use_time, "\
                 "timestamp_v)"\
                 "VALUES(%d, %d, %s, %s, %s, %s, %s, %s, %s, %d, %d, %d, %s, %s, %s, %s, %s, %s, %s)"
    a = etlLog.__str__()
    print(a)
   # conn.execute(sql,a)
    print(sql)

if __name__ == '__main__':
    sendEtlLogGetId(EtlLog(72, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None))

