from dao.DBServer import *
from domain.datasyncBean import *

from domain.datasyncBean import Stepstats, Datarelation, Topic


def get_app_row_sql(id, lab):
    sql = """
        select 
            t4.table_code as front_talbe_code
            ,t4.table_name as front_talbe_name
            ,ifnull(t3.exec_state,'stop') as front_table_state
        from t_table_base t1 left join t_table_relation t2 on t1.id=t2.behind_table_id 
        left join v_log_daily t3 on t2.front_table_id = t3.config_id
        left join t_table_base t4 on t2.front_table_id=t4.id
        where  t1.table_lab ='app' 
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
        if datum[2] == 'success':
            flag_success = flag_success + 1
        elif datum[2] == 'fal':
            flag_fal = flag_fal + 1
        elif datum[2] == 'stop':
            flag_stop = flag_stop + 1
    if flag_fal != 0:
        stats = 'FAI'
    if flag_success != 0 and flag_stop != 0 and flag_fal == 0:
        stats = 'ING'
    if flag_stop == 0 and flag_fal == 0 and flag_success != 0:
        stats = 'SUC'
    if flag_stop != 0 and flag_fal == 0 and flag_success ==0:
        stats = 'STOP'

    if stats == 'FAI':
        title = '节点执行失败'
    elif stats == 'ING':
        title = '节点正在运行'
    elif stats == 'STOP':
        title = '节点未开始执行'
    else:
        title = '节点执行成功'

    if stats == 'FAI':
        for datum in data:
            if datum[2] == 'stop':
               memo = datum[0]+'-'+datum[1]+'  '

    # 三个属性值拼接完成构造对象

    return Stepstats(stats,title,memo)



def pandect():

    # 获取数据库链接对象
    conn = get_connect()
    topic_list = []
    # 从t_table_base 表中获取主题层表表id
    sql = "select id,table_name,table_code from t_table_base t1 where t1.table_lab='app'"
    result = conn.query(sql)
    for row in result:
        if len(row) != 0:
            topicname = row[1]
            topictable = row[2]
            topictime = None

            #获取节点执行时间
            re = get_connect().query("select timestamp_v  from v_log_daily where config_id = '" + str(row[0]) + "'")
            if len(re) != 0:
                topictime = re[0][0].strftime("%Y-%m-%d %H:%M:%S")
            dataget = get_front_state(row[0],'src')
            datahandle = Stepstats(dataget.stats,'','')
            datavalidate = Stepstats(dataget.stats,'','')
            datawrit = Stepstats(dataget.stats,'','')
            datarelationlist = []
            #获取表依赖关系
            relation_result=conn.query("select t2.table_code ,t2.table_name from t_table_relation t1 left join t_table_base t2  on t1.front_table_id = t2.id where t1.behind_table_id='"+str(row[0])+"'")
            for relation in relation_result:
                if len(relation) != 0:
                    datarelationlist.append(Datarelation('',relation[0],relation[1],'','',''))
            topic= Topic(topicname,topictable,topictime,dataget,datahandle,datavalidate,datawrit,datarelationlist)
            topic_list.append(topic)
    return topic_list


def pandect_topic():
    data = []
    dataget = Stepstats('SUC', '', '')
    datahandle = Stepstats('WAR', '数据缺失', 'wx_order微信订单 - 数据更新异常,pos_order线下订单 - 数据更新异常')
    datavalidate = Stepstats('FAI', '处理失败', '数据缺失')
    datawrit = Stepstats('STOP', '未执行', '此节点未执行')
    datarelationlist = [Datarelation('', 'wx_order', '微信订单', '', '', ''),
                        Datarelation('', 'pos_order', '线下订单', '', '', ''),
                        Datarelation('', 'tm_order', '淘宝订单', '', '', '')]
    data.append(Topic('app_order_item', 'app_order_item', '2020-11-10 15:00:00', dataget, datahandle, datavalidate, datawrit, datarelationlist))
    return data


def pandect_table():
    data = []
    datarelationlist = [Datarelation('', '', '', '', 'app_order', '订单主题'),
                        Datarelation('', '', '', '', 'app_member', '会员主题'),
                        Datarelation('', '', '', '', 'app_guide', '导购主题')]
    syncstats = Stepstats('SUC', '一切正常', '这里看起来没什么信息')
    data.append(Table('crm_shop', '1', 'src_shop', '店铺信息', '全渠道店铺基础信息', syncstats, '2020-01-01 15:37', '1', '2020-01-01~2020-01-07', datarelationlist))
    return data





if __name__ == '__main__':
    # data = pandect()
    # print(data.topicname, data.datawrit)
    # if data.topicname[0] == '123':
    #     print(True)
    # else:
    #     print(False)
    # test()
    print(pandect())