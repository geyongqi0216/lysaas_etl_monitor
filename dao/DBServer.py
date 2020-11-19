import datetime
import re
import pymysql
import logging

from dao import setting


class Connect:

    def _trim(self, s):
        if s.startswith(' ') or s.endswith(' '):
            return re.sub(r"^(\s+)|(\s+)$", "", s)
        return s

    def insert(self, tab_name, data, columns=None):
        """
        入库
        :param tab_name: 表名
        :param data: 数据
        :param columns: 指定表字段
        :return:
        """
        logging.error('Connect.insert code implementation!')
        raise Exception('Connect.insert code implementation!')

    def query(self, sql):
        """
        查询
        :param sql: 查询sql
        :return: 返回数据
        """
        logging.error('Connect.query code implementation!')
        raise Exception('Connect.query code implementation!')

    def execute(self, sql):
        """
        执行sql
        :param sql: 执行的sql
        :return: 执行结果
        """
        logging.error('Connect.execute code implementation!')
        raise Exception('Connect.execute code implementation!')

    def close(self):
        """
        关闭数据库连接
        :return:
        """
        logging.error('Connect.close code implementation!')

    def gen_count(self, tab_name):
        """
        生成统计语句
        :param tab_name:
        :return:
        """
        sql = "select count(1) as cnt from " + tab_name
        # TODO 特殊表处理
        if tab_name == 'src_customer_assets_distribution_log_models':
            sql = "select count(1) from " + tab_name + " where DistributionTime >= '"+_get_datetime(60*24*30)+"';"
        return sql

    def gen_truncate(self, tab_name):
        """
        生成清空表语句
        :param tab_name:
        :return:
        """
        sql = "truncate table " + tab_name
        return sql

    def gen_query(self, tab_name, select_column=None, where_condition=None, order_by=None, limit_num=None, offset_num=None):
        """
        生成查询sql
        :param tab_name: 表名
        :param select_column: 查询字段列表
        :param where_condition: 查询条件
        :param order_by: 排序字段
        :param limit_num: 限制查询行数
        :param offset_num: 查询其实行数
        :return:
        """
        if select_column is None:
            sql = "select * from " + tab_name
        else:
            sql = "select " + select_column + " from " + tab_name
        if where_condition is not None:
            sql = sql + " " + where_condition
        if order_by is not None:
            sql = sql + " order by " + order_by
        if limit_num is not None and offset_num is not None:
            sql = sql + " limit " + str(limit_num) + " offset " + str(offset_num)
        elif limit_num is not None:
            sql = sql + " limit " + str(limit_num)
        elif offset_num is not None:
            sql = sql + " offset " + str(offset_num)
        return sql

    def gen_delete(self, tab_name, where_condition):
        """
        生成删除sql
        :param tab_name: 表名
        :param where_condition: 查询条件
        :return:
        """
        if where_condition is None:
            where_condition = ""
        sql = "delete from "+tab_name+" "+where_condition;
        return sql

    def gen_delete_by_mid(self, tab_name, tab_pk):
        """
        增量数据同步，生成删除sql
        :param tab_name: 表名
        :return:
        """
        sql = self.gen_delete(tab_name, "where ("+tab_pk+") in (select "+tab_pk+" from "+tab_name+"_mid)")
        return sql

    def gen_insert_by_mid(self, tab_name, tab_columns):
        """
        增量数据同步，中间表处理
        :param tab_name:
        :param tab_columns:
        :return:
        """
        sql = "insert into " + tab_name + "(" + tab_columns + ") select " + tab_columns + " from " + tab_name + "_mid"
        logging.info(sql)
        return sql


class MysqlSingleConnect(Connect):
    """
    没有结束时自动关闭数据库连接功能，使用时请在调用结束后手动关闭连接
    """

    def __init__(self):
        self._get_connect()

    def _get_connect(self):
        self.conn = pymysql.connect(host=setting.elt_database_host,
                                    port=setting.elt_database_port,
                                    user=setting.elt_database_username,
                                    password=setting.elt_database_password,
                                    database=setting.elt_database_db,
                                    charset=setting.elt_database_charset)
        self.csr = self.conn.cursor()

    def query(self, sql):
        logging.debug(sql)
        self.csr.execute(sql)
        return self.csr.fetchall()

    def execute(self, sql,args=None):
        logging.debug(sql)
        result = self.csr.execute(sql,args)
        self.conn.commit()
        logging.debug(result)
        return result

    def close(self):
        try:
            self.csr.close()
            self.conn.close()
        except Exception as e:
            logging.error('close connection error ,result:{}'.format(e))


class MysqlConnect(MysqlSingleConnect):

    """
        Mysql数据库
    """
    def _get_connect(self):
        self.conn = pymysql.connect(host=setting.mysql_database_host,
                                    port=setting.mysql_database_port,
                                    user=setting.mysql_database_username,
                                    password=setting.mysql_database_password,
                                    database=setting.mysql_database_db,
                                    charset=setting.mysql_database_charset)
        self.csr = self.conn.cursor()


def get_connect():
    return MysqlConnect()


