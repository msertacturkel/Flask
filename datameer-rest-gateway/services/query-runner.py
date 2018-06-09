from services.MysqlConsumer import MysqlConsumer

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

