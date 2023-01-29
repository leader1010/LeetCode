from sql_practice.leetcode_database import LeetCodeDataBase

if __name__ == '__main__':
    database = LeetCodeDataBase()
    sqls = """Create table If Not Exists Employee (Id int, Salary int)
Truncate table Employee
insert into Employee (id, salary) values ('1', '100')
insert into Employee (id, salary) values ('2', '200')
insert into Employee (id, salary) values ('3', '300')"""
    sql_list = sqls.split('\n')
    for sql in sql_list:
        database.execute_sql(sql)
    query_sql = """CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select distinct a.salary from 
      (select salary, dense_rank() over (order by salary desc) rank_s from employee) a
      where rank_s=n
      
  );
END"""
    # query_sql = 'select * from employee order by salary desc'
    database.query_data(query_sql)
    database.close_connect()
