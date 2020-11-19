from dao.DBServer import get_connect
from domain.datasyncBean import Stepstats, Datarelation, Topic, Table


def get_app_row_sql(id, lab):
    sql = """
        select 
            t4.table_code as front_talbe_code
            ,t4.table_name as front_talbe_name
            ,ifnull(t3.exec_state,'STOP') as front_table_state
        from t_table_base t1 left join t_table_relation t2 on t1.id=t2.behind_table_id 
        left join v_log_daily t3 on t2.front_table_id = t3.config_id
        left join t_table_base t4 on t2.front_table_id=t4.id
        where  t1.table_lab ='topic' 
    """
    sql = sql+"and t1.id='"+id+"'"
    sql = sql+"and t4.table_lab='"+lab+"'"

    return sql


# 计算某个主题依赖的步骤执行状态，id 主题id,level 依赖层级
def get_front_state(id,level):
    flag_success = 0
    flag_stop = 0
    flag_fal = 0
    stats = ''
    title = ''
    memo = ''
    data = get_connect().query(get_app_row_sql(str(id), level))
    for datum in data:
        if datum[2] == 'SUC':
            flag_success = flag_success + 1
        elif datum[2] == 'FAI':
            flag_fal = flag_fal + 1
        elif datum[2] == 'STOP':
            flag_stop = flag_stop + 1
    if flag_fal != 0:
        stats = 'FAI'
    if flag_success != 0 and flag_stop != 0 and flag_fal == 0:
        stats = 'ING'
    if flag_stop == 0 and flag_fal == 0 and flag_success != 0:
        stats = 'SUC'
    if flag_stop != 0 and flag_fal == 0 and flag_success ==0:
        stats = 'STOP'
    # 默认没有配置relation表的话节点默认成功
    if flag_success + flag_fal + flag_stop ==0:
        stats = 'SUC'

    if stats == 'FAI':
        title = '以下任务执行异常'
    elif stats == 'ING':
        title = '节点正在运行'
    elif stats == 'STOP':
        title = '节点未开始执行'
    else:
        title = '节点执行成功'

    if stats == 'FAI':
        for datum in data:
            if datum[2] == 'FAI':
               memo = datum[0]+'-'+datum[1]+' , '

    # 三个属性值拼接完成构造对象

    return Stepstats(stats,title,memo)


# 主函数
def pandect_topic():
    # 获取数据库链接对象
    conn = get_connect()
    topic_list = []
    # 从t_table_base 表中获取主题层表表id
    sql = "select id,table_name,table_code from t_table_base t1 where t1.table_lab='topic'"
    rows = conn.query(sql)
    if len(rows) == 0:
        return topic_list
    for row in rows:
        topicname = None
        topictable = None
        topictime = '今日未完成'
        dataget = None
        datahandle = None
        datavalidate = None
        datawrit = None
        datarelationlist = None

        # 给属性赋值
        topicname = row[1]
        topictable = row[2]
        #获取节点执行时间
        re = get_connect().query("select timestamp_v  from v_log_daily where config_id = '" + str(row[0]) + "'")
        if len(re) != 0:
            topictime = re[0][0].strftime("%Y-%m-%d %H:%M:%S")
        # step1 数据获取
        dataget = get_front_state(row[0],'src')
        if dataget.stats == 'FAI' or dataget.stats == 'STOP':
            datahandle = Stepstats('STOP','提示','前置节点失败')
        else:
            datahandle = get_front_state(row[0],'exec')

        if datahandle.stats == 'FAI' or datahandle.stats == 'STOP' :
            datavalidate = Stepstats('STOP','提示','前置节点失败')
        else:
            datavalidate = get_front_state(row[0],'check')

        if datavalidate.stats == 'FAI' or datavalidate.stats == 'STOP':
            datawrit = Stepstats('STOP','提示','前置节点失败')
        else:
            datawrit = get_front_state(row[0],'topic')

        datarelationlist = []
        #获取表依赖关系
        relation_result=conn.query("select t2.table_code ,t2.table_name from t_table_relation t1 left join t_table_base t2  on t1.front_table_id = t2.id where t1.behind_table_id='"+str(row[0])+"'")
        for relation in relation_result:
            if len(relation) != 0:
                datarelationlist.append(Datarelation('',relation[0],relation[1],'','',''))
        topic = Topic(topicname,topictable,topictime,dataget,datahandle,datavalidate,datawrit,datarelationlist,'')
        topic_list.append(topic)
    return topic_list


def pandect_topic_demo():
    data = []
    dataget = Stepstats('SUC', '', '')
    datahandle = Stepstats('WAR', '数据缺失', 'wx_order微信订单 - 数据更新异常,pos_order线下订单 - 数据更新异常')
    datavalidate = Stepstats('FAI', '处理失败', '数据缺失')
    datawrit = Stepstats('STOP', '未执行', '此节点未执行')
    datarelationlist = [Datarelation('', 'wx_order', '微信订单', '', '', ''),
                        Datarelation('', 'pos_order', '线下订单', '', '', ''),
                        Datarelation('', 'tm_order', '淘宝订单', '', '', '')]
    dashboardlist = [Datarelation('', '', '', '', 'dabo_order', '销售类报表'),
                        Datarelation('', '', '', '', '', '商品类报表'),
                        Datarelation('', '', '', '', 'dabo_guide', '导购类报表')]
    data.append(Topic('app_order', '订单主题', '2020-11-10 15:00:00', dataget, datahandle, datavalidate, datawrit, datarelationlist,dashboardlist))
    return data


def pandect_table_demo():
    data = []
    datarelationlist = [Datarelation('', '', '', '', 'app_order', '订单主题'),
                        Datarelation('', '', '', '', 'app_member', '会员主题'),
                        Datarelation('', '', '', '', 'app_guide', '导购主题')]
    syncstats = Stepstats('SUC', '一切正常', '这里看起来没什么信息')
    data.append(Table('crm_shop', '1', 'src_shop', '店铺信息', '全渠道店铺基础信息', syncstats, '2020-01-01 15:37', '99', '2020-01-01~2020-01-07', datarelationlist))
    return data


def pandect_table():
    tables = []
    rows = get_connect().query("select t1.id , t1.table_code , t1.table_name , ifnull(t1.remark,'') , ifnull(t1.source_table_code,'') ,ifnull(t2.exec_state,'STOP') , ifnull(t2.task_end_time,'') , ifnull(t2.target_number,'') , ifnull(t2.sync_condition,'') from t_table_base t1 left join v_log_daily t2 on t1.id = t2.config_id where table_lab ='src'")
    if len(rows) == 0:
        return tables
    for row in rows:
        # 获取到每一张src_表的信息
        sourcetablename = ''
        tableid = ''
        targettablename = ''
        tablename = ''
        remark = ''
        syncstats = None
        synctime = ''
        syncappend = ''
        synccondition = ''
        datarelationlist = []
        sourcetablename = row[4]
        tableid = row[0]
        targettablename =row[1]
        tablename =row[2]
        remark = row[3]
        synctime = row[6]
        syncappend = row[7]
        synccondition =  row[8]
        syncstats = Stepstats(row[5],'提示','测试')

        data = get_connect().query("select t2.id,t2.table_code,t2.table_name from t_table_relation t1 left join t_table_base t2 on t1.behind_table_id = t2.id and t2.table_lab ='topic' where  t1.front_table_id='" + str(row[0]) +"'")
        for tb in data:
            datarelationlist.append(Datarelation('','','',tb[0],tb[1],tb[2]))
        tables.append(Table(sourcetablename,tableid,targettablename,tablename,remark,syncstats,synctime,syncappend,synccondition,datarelationlist))
    return tables


if __name__ == '__main__':
    sql="insert into t_job_log (config_id,exec_state,timestamp_v) values('31','SUC','2020-11-12 16:00:00')"
    conn=get_connect()
    insert_result = conn.execute(sql)
    data = conn.query("select LAST_INSERT_ID()")
    print(insert_result)
    print(data[0][0])