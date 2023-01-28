from sql_practice.leetcode_database import LeetCodeDataBase

if __name__ == '__main__':
    database = LeetCodeDataBase()

    sqls = """Create table If Not Exists Person (personId int, firstName varchar(255), lastName varchar(255))
Create table If Not Exists Address (addressId int, personId int, city varchar(255), state varchar(255))
Truncate table Person
insert into Person (personId, lastName, firstName) values ('1', 'Wang', 'Allen')
insert into Person (personId, lastName, firstName) values ('2', 'Alice', 'Bob')
Truncate table Address
insert into Address (addressId, personId, city, state) values ('1', '2', 'New York City', 'New York')
insert into Address (addressId, personId, city, state) values ('2', '3', 'Leetcode', 'California')"""
    sql_list = sqls.split("\n")
    # print(sql_list)
    for sql in sql_list:
        database.execute_sql(sql)

    query_sql = """
select firstname,lastName,city,state from person p left join address a on p.personid = a.personid
    """
    database.query_data(query_sql)
    database.close_connect()
