练习1： 使用book表完成

1. 统计每位作家写的图书的平均价格

select author,avg(price) from book group by author;

2. 统计每个出版社出版图书的数量
select publication,count(*) from book group by puclication;

3. 查看总共有多少个出版社
select count(distinct publication) from book;

4. 筛选出 那些出版过超过50的图书的出版社，并按照图书最高价格排序
select publication,max(price)
from book
group by publication
having max(price) > 50
order by max(price) desc;

5. 统计相同出版时间的图书的平均价格
select publication_time,avg(price) from book group by publication_time;


索引示例

create table index_test (id int primary key auto_increment,name varchar(20),index name_index(name));