from sql_practice.leetcode_database import LeetCodeDataBase

if __name__ == '__main__':
    database = LeetCodeDataBase()
    sqls = """Create table If Not Exists Employee (id int, salary int)
Truncate table Employee
insert into Employee (id, salary) values ('1', '100')
insert into Employee (id, salary) values ('2', '200')
insert into Employee (id, salary) values ('3', '300')"""
    sql_list = sqls.split("\n")
    for sql in sql_list:
        database.execute_sql(sql)
    #     嵌套一次select 满足没有第二高时返回null的要求
    sql = "select (select distinct salary from employee order by salary desc limit 1 offset 1) SecondHighestSalary"
    database.query_data(sql)
    database.close_connect()
