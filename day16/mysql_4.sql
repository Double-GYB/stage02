-- E-R模型中学生  教师   课程表的建立
create table stu(
id int primary key auto_increment,
姓名 varchar(30),
年龄 tinyint,
性别 char,
籍贯 varchar(128)
);

create table teacher(
id int primary key auto_increment,
姓名 varchar(30),
职称 varchar(30),
年龄 tinyint
);

create table course(
id int primary key auto_increment,
名称 varchar(30),
学分 float,
tid int,
constraint  t_fk
foreign  key (tid)
references teacher(id)
);

create table course_stu(
cid int,
sid int,
score float,
primary key(cid,sid),
constraint  c_fk
foreign  key (cid)
references course(id),
constraint  s_fk
foreign  key (sid)
references stu(id)
);


关联查询练习 使用cls 和 interest
1 学生对应的爱好和兴趣班的价格
select cls.name,interest.hobby,interest.price from  cls inner join interest on cls.name=interest.name;

2 查询所有班级学生信息，同时标注出哪些同学有什么样的兴趣爱好
select c.name,c.sex,i.hobby from cls as c left join interest as i on c.name=i.name;

3 查看所有兴趣爱的信息，并且标注与其对应的同学
select i.hobby,i.price,c.name from cls as c right join interest as i on c.name=i.name;