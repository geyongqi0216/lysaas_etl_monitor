import psycopg2
import psycopg2.extras as ext
import logging


def user_info():
    conn = psycopg2.connect(host='39.100.112.239', user='gpadmin', password='#zi6_%~', database='user')
    cursor = conn.cursor()
    return cursor


def dl_sql():
    cursor = user_info()
    logging.debug('select user_name,pass_word from user_info')
    cursor.execute('select user_name,pass_word from user_info')
    rows = cursor.fetchall()
    return rows


def zc_sql(username, password):
    cursor = user_info()
    logging.debug(f'INSERT INTO user_info (user_name,pass_word) VALUES (\'{username}\', \'{password}\')')
    cursor.execute(f'INSERT INTO user_info (user_name,pass_word) VALUES (\'{username}\', \'{password}\')')
    cursor.connection.commit()
    return


if __name__ == '__main__':
    data = user_info()
    for i in data:
        print(i[0])
