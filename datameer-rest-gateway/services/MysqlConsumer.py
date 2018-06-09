# -*- coding: utf-8 -*-
'''mysql client kurulu olmalı pip install mysqlclient==1.3.4'''
import MySQLdb, yaml

from services.DBConsumer import DBConsumer


class MysqlConsumer(DBConsumer):
    def __init__(self):
        self.HOST = ''
        self.USER = ''
        self.PASSWD = ''
        self.DBNAME = ''

    def read_config(self):
        with open("../config/mysql-config.yml", 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
            self.HOST = cfg['mysql']['host']
            self.USER = cfg['mysql']['user']
            self.PASSWD = cfg['mysql']['passwd']
            self.DBNAME = cfg['mysql']['db']

    def connect_db(self):
        db = MySQLdb.connect(host=str(self.HOST),  # your host
                             user=str(self.USER),  # username
                             passwd=str(self.PASSWD),  # password
                             db=str(self.DBNAME))  # name of the database
        return db

    def execute_query(self, query):
        print query
        db = self.connect_db()
        # Create a Cursor object to execute queries.
        cur = db.cursor()
        # Select data from table using SQL query.

        cur.execute(query)
        result = cur.fetchall()
        self.print_result(result)
        return result

    @staticmethod
    def print_result(result):
        for row in result:
            print row
        print "-------------------------------------------------------------------------"


if __name__ == '__main__':
    mysqlConsumer = MysqlConsumer()
    mysqlConsumer.read_config()
    #first query
    q1 = "select concat(table_name, '.', column_name) as 'foreign key', concat(referenced_table_name, '.', referenced_column_name) as 'references' " \
         "from information_schema.key_column_usage " \
         "where " \
         "referenced_table_name is not null " \
         "and table_schema = 'a'"

    mysqlConsumer.execute_query(q1)

    #select updated views
    q2 = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='VIEW' AND UPDATE_TIME IS NOT NULL"
    mysqlConsumer.execute_query(q2)

    # select updated tables
    q3 = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND UPDATE_TIME IS NOT NULL"
    mysqlConsumer.execute_query(q3)
    q4 ="SELECT * FROM a.APP_USER"
    mysqlConsumer.execute_query(q4)

