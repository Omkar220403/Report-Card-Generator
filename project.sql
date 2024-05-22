show databases;
use reportcard;
drop table if exists student;
create table student(Name char(20), Class char(20), Division char(10), Roll_no int primary key, Status char(15));
select * from student;

create table marks(Roll_no int primary key,Division char(10), Semester int, Session varchar(15), 
PP int(5), DS int(5), DBMS int(5), CN int(5), AM int(5));
select * from marks;