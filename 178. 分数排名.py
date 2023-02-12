from sql_practice.leetcode_database import LeetCodeDataBase

if __name__ == '__main__':
    database = LeetCodeDataBase()
    sqls = """Create table If Not Exists Scores (id int, score DECIMAL(3,2))
Truncate table Scores
insert into Scores (id, score) values ('1', '3.5')
insert into Scores (id, score) values ('2', '3.65')
insert into Scores (id, score) values ('3', '4.0')
insert into Scores (id, score) values ('4', '3.85')
insert into Scores (id, score) values ('5', '4.0')
insert into Scores (id, score) values ('6', '3.65')"""
    sql_list = sqls.split('\n')
    for sql in sql_list:
        database.execute_sql(sql)
    # database.query_data("select a.Score Score, (select count(destinct b.Score) from Scores b where b.Score >=a.Score) as rank from Scores a order by a.score desc")
    database.query_data("select a.Score as Score,(select count(distinct b.Score) from Scores b where b.Score >= a.Score) as Rank from Scores a order by a.Score DESC")
    # SELECT
    # a.Score, COUNT(DISTINCT
    # b.Score) AS
    # `RANK`
    # FROM
    # Scores
    # a, Scores
    # b
    # WHERE
    # a.Score <= b.Score
    # GROUP
    # BY
    # a.Id
    # ORDER
    # BY
    # `RANK`;
    database.close_connect()


