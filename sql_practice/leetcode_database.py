import pymysql


class LeetCodeDataBase(object):
    def __init__(self, host='localhost', port=3306, user='root', password='b930327366',
                 database='mysql_leetcode', charset='utf8'):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password,
                                    database=database, charset=charset)
        self.cursor = self.conn.cursor()

    def execute_sql(self, sql):
        try:
            # 执行 SQL 语句
            row_count = self.cursor.execute(sql)
            # print("SQL 语句执行影响的行数%d" % row_count)
            # 提交数据到数据库
            self.conn.commit()
        except Exception as e:
            # 回滚数据， 即撤销刚刚的SQL语句操作
            self.conn.rollback()

    def query_data(self, sql):
        self.cursor.execute(sql)
        # 取出结果集中一行数据,　例如:(1, '张三')
        # print(cursor.fetchone())
        # 取出结果集中的所有数据, 例如:((1, '张三'), (2, '李四'), (3, '王五'))
        for line in self.cursor.fetchall():
            print(line)

    def close_connect(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()
