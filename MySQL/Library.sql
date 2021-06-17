1. 도서 대출 현황 데이터베이스 생성

create database library;


2. 각 테이블(학생,도서,대출현황) 생성

-학생 정보를 담은 학생 테이블(학생ID,이름) 생성

create table student
    -> (studentid int not null,
    -> name char(10) not null,
    -> primary key(id)
    -> );

-도서 정보를 담은 테이블(도서명,도서번호) 생성

create table book
    -> (bookname varchar(50) not null,
    -> bookid int not null,
    -> primary key (bookid)
    -> );

-도서 대출 현황 정보를 담은 테이블(대출번호, 학생ID, 도서번호, 대출현황) 생성

create table lent
    -> (no int not null,
    -> studentid int not null,
    -> bookid int not null,
    -> lent int not null,
    -> primary key (no, studentid, bookid)
    -> );


3. 각 테이블에 정보 입력

-학생 테이블에 정보(학생ID,이름) 입력
insert into student values
    -> (1, 'kim'),
    -> (2, 'lee'),
    -> (3, 'park'),
    -> (4, 'choi'),
    -> (5, 'han'),
    -> (6, 'jeong'),
    -> (7, 'jong'),
    -> (8, 'yang'),
    -> (9, 'joe'),
    -> (10, 'min');

-도서 테이블에 도서 정보(도서명,도서번호) 입력

insert into book values
    -> ('a', 11),
    -> ('b', 22),
    -> ('c', 33),
    -> ('d', 44),
    -> ('e', 55),
    -> ('f', 66),
    -> ('g', 77),
    -> ('h', 88),
    -> ('i', 99),
    -> ('j', 00);


-대출 현황 테이블 정보(대출번호, 학생ID, 도서번호, 대출현황) 입력
대출현황 = 1 이면 대출된 도서를 뜻함

insert into lent values
-> (1, 1, 11, 1),
    -> (2, 2, 22, 1),
    -> (3, 3, 33, 1),
    -> (4, 4, 44, 0),
    -> (5, 5, 55, 0),
    -> (6, 6, 66, 1),
    -> (7, 7, 77, 1),
    -> (8, 8, 88, 0),
    -> (9, 9, 99, 0),
    -> (10, 10, 0, 0);


4. 테이블 정보 입력 확인

- 학생정보 테이블 확인
Select * from student;

-도서정보 테이블 확인
Select * from book;

-도서 대출 현황 테이블 확인
Select * from lent;

 
5. 대여된 도서명과 학생명 SELECT 문으로 작성하기

SELECT book.bookname, student.name
    -> FROM lent INNER JOIN book
    -> on lent.bookid = book.bookid
    -> INNER JOIN student
    -> on lent.studentid = student.studentid
    -> WHERE lent = 1;

 

