--create table If Not Exists Employee (Id int, Salary int)
--truncate table Employee
--insert into Employee (id, salary) values ('1', '100')
--insert into Employee (id, salary) values ('2', '200')
--insert into Employee (id, salary) values ('3', '300')

select max(a.salary) SecondHighestSalary from (select salary from Employee order by salary desc limit 1 offset 1) a;