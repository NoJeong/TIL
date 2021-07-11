# SQL TUTORIAL



*--한줄주석*

*/\*여러줄 주석\*/*



*-- 테이블 정보 조회*

SELECT * FROM classmates;



 *-- data 입력(CREATE)*



INSERT INTO classmates (name,age)

VALUES ('홍길동',23);



 *-- 모든 컬럼을 입력할때는 컬럼을 생략가능*



INSERT INTO classmates

VALUES ('hong',30,'seoul');



*-- 컬럼의 위치는 qusrud 가능 단 value 도 위치 확인해야함*



INSERT INTO classmates (age,name)

VALUES (23,'홍길동');



*-- id를 보고 싶을때*

SELECT rowid, * FROM classmates;



*-- 테이블 다시 정의 (id, not null 적용)*

 *-- 기존테이블 삭제*

DROP TABLE classmates;



 *-- 테이블 재정의*

CREATE TABLE classmates(

 id INTEGER PRIMARY KEY,

 name TEXT NOT NULL,

 age INT NOT NULL,

 address TEXT NOT NULL

);



*-- rowid를 사용하기위해 정의한 id 삭제*

CREATE TABLE classmates(

 name TEXT NOT NULL,

 age INT NOT NULL,

 address TEXT NOT NULL

);



*-- INSERT INTO로 값을 한번에 넣는 방법*

INSERT INTO classmates VALUES ('HONG',30,'seoul'),('kim',23,'daejeon'),('park',23,'gwangju'),('lee',33,'gumi');



*-- classmates에서 id 와 name 을 가져오고싶다면*

SELECT rowid, name FROM classmates;



*-- 정해진 갯수만 보고싶다면*

SELECT rowid, name FROM classmates LIMIT num;



*-- 특정 위치에서부터 몇개만 가져온다면?*

SELECT rowid, name FROM classmates LIMIT num OFFSET index;

*-- 세번째 있는 값 하나만 가져오고싶다*

SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

*-- 주소가 서울인 사람만 가져오고 싶다.* 

SELECT rowid, name FROM classmates WHERE address='seoul';

*-- age값을 중복없이 가져오고 싶을떄*

SELECT DISTINCT age FROM classmates;

*-- id 가 4인 레코드를 삭제하는법*

DELETE FROM classmates WHERE rowid=4;

*-- id가 4 인 레코드의 이름은 kang 주소는 jeju로 수정*

UPDATE classmates SET name = 'KANG', address='JEJU' WHERE rowid=4;



*-- user data를 새롭게 테이블로 작서*

*-- 선행되어야할게 users.csv 파일이 db파일과 동일한 위치에 있어야함* 

*-- sqlite에서 사용하는 dot command*

.table # 모든테이블 확인

.mode csv #현재 보여지는 형태를 csv로 변환

.import users.csv users 라는 테이블 생성

SELECT * FROM users;



*-- 30살 이상 데이터 가져오고 싶을때*

SELECT * FROM users WHERE age>=30;

*-- 30살 이상이고 성이 김인 사람의 성과 나이*

SELECT last_name, age FROM users WHERE age>29 and last_name="김";

*-- users ㅔ이블의 모든 레코드 갯수*

SELECT COUNT(*) FROM users;

*-- 30살 이상의 평균나이는*

SELECT AVG(age) FRom users WHERE age>=30;

*-- 계좌잔액 가장 높은 사람과 그 금액*

SELECT MAX(balance), first_name FROM users;

*-- 30살 이상인 사람의 계좌 평균 잔액은?*

SELECT AVG(balance) FROM users WHERE age>=30;

*-- 20대인 사람은?*

SELECT * FROM users WHERE age like '2_';

*-- 지역번호가 02 인 사람*

SELECT * FROM users WHERE phone like '02-%';

*-- 이름이 '준'으로 끝나는 사람*

SELECT * FROM users WHERE first_name like '%준';

*-- 가운데 번호가 5114 인 사람*

SELECT * FROM users WHERE phone like '%-5114-%';

*-- 나이순 오름차순으로 10명만*

SELECT * FROM users ORDER BY age ASC LIMIT 10;

*-- 각 성씨의 명수 확인*

SELECT last_name, COUNT(*) FROM users GROUP BY last_name;

*-- 각 성씨의 명수를 확인 AS를 활용해서 컬럼명을 설정*

SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;