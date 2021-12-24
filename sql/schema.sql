-- drop book table
drop table if exists book;

-- create book table if it does not exist
create table book
(
  book_id         char(8)   primary key   not null,
  book_name       char(50)                not null,
  book_isbn       char(17)                not null,
  book_author     char(10)                not null,
  book_publisher  char(50)                not null,
  book_price      real                    not null,   
  interview_times smallint                not null
);

-- insert values into book table
insert into book (book_id, book_name, book_isbn, book_author, book_publisher, book_price, interview_times)
values ('b0001', 'SQL Server 2012 宝典 ', '978-7-121-22013-5', '廖梦怡', '电子工业出版社', 89.00, 18);

insert into book (book_id, book_name, book_isbn, book_author, book_publisher, book_price, interview_times)
values ('b0002', '职称英语专用教材', '978-7-121-14800-2', '孙若红', '电子工业出版社', 45.00, 35);

insert into book (book_id, book_name, book_isbn, book_author, book_publisher, book_price, interview_times)
values ('b0003', '中国通史', '978-7-5388-53155', '于海娣', '黑龙江科学技术出版社', 68.00, 25);

insert into book (book_id, book_name, book_isbn, book_author, book_publisher, book_price, interview_times)
values ('b0004', '丰子恺儿童文学选集', '978-7-5007-8972-7', '丰子恺', '中国少年儿童出版社', 22.50, 40);

insert into book (book_id, book_name, book_isbn, book_author, book_publisher, book_price, interview_times)
values ('b0005', '英语同义词辨析词典', '978-7-5135-2294-6', '赵同水', '外语教学与研究出版社', 55.00, 6);

insert into book (book_id, book_name, book_isbn, book_author, book_publisher, book_price, interview_times)
values ('b0006', '数据库基础与应用', '978-7-304-06430-3', '徐孝凯', '中央广播电视大学出版社', 35.00, 5);

insert into book (book_id, book_name, book_isbn, book_author, book_publisher, book_price, interview_times)
values ('b0007', '微积分初步', '978-7-304-03742-0', '赵坚', '中央广播电视大学出版社', 17.00, 4);

insert into book (book_id, book_name, book_isbn, book_author, book_publisher, book_price, interview_times)
values ('b0008', 'ASP.NET 从入门到精通', '978-7-302-28753-7', '明日科技', '清华大学出版社', 89.80, 27);