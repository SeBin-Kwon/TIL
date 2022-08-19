# 🥎 WHERE

#### Table users 생성

```sql
CREATE TABLE users ( 
    first_name TEXT NOT NULL, 
    last_name TEXT NOT NULL, 
    age INTEGER NOT NULL, 
    country TEXT NOT NULL, 
    phone TEXT NOT NULL, 
    balance INTEGER NOT NULL
);
```

#### csv파일 정보를 테이블에 적용하기

```sql
.mode csv
.import users.csv users
.tables
classmates examples users
```

#### 특정 조건으로 데이터 조회하기

```sql
SELECT * FROM 테이블이름 WHERE 조건;
```

<br>

### WHERE절에서 사용할 수 있는 연산자

- 비교 연산자
  - `=`, `>`, `>=`, `<`, `<=`는 숫자 혹은 문자 값의 대/소, 동일 여부를 확인하는 연산자
- 논리 연산자
  - `AND`
    - 앞에 있는 조건과 뒤에 오는 조건이 모두 참인 경우
  - `OR`
    - 앞의 조건이나 뒤의 조건이 참인 경우
  - `NOT`
    - 뒤에 오는 조건의 결과를 반대로

<br>

### 🚨 주의!

```sql
-- 1. 키가 175이거나, 키가 183이면서 몸무게가 80인 사람
WHERE HEIGHT = 175 OR HEIGHT = 183 AND WEIGHT = 80

-- 2. 키가 175 또는 183인 사람 중에서 몸무게가 80인 사람 
WHERE (HEIGHT = 175 OR HEIGHT = 183) AND WEIGHT = 80
```

- 웬만하면 괄호치자!

<br>

### SQL 사용할 수 있는 연산자

- `BETWEEN 값1 AND 값2`

  - 값1과 값2 사이의 비교 (값1 <= 비교값 <= 값2)

  ```sql
  SELECT COUNT(*) FROM healthcare WHERE height BETWEEN 160 AND 170;
  ```

- `IN (값1, 값2, ...)`

  - 목록 중에 값이 하나라도 일치하면 성공

- `LIKE`

  - 비교 문자열과 형태 일치
  - 와일드카드 (`%` : 0개 이상 문자, `_` : 1개 단일 문자)

- `IS NULL / IS NOT NULL`

  - NULL 여부를 확인할 때는 항상 `=` 대신에 `IS`를 활용

- 부정연산자

  - 같지 않다. (`!=`,` ^=`, `<>`)
  - ~와 같지 않다. (`NOT 칼럼명=`)
  - ~보다 크지 않다. (`NOT 칼럼명>`)

  ```sql
  WHERE 칼럼명1 != 비교값1
  AND 칼럼명2 ^= 비교값2
  AND 칼럼명3 <> 비교값3
  AND NOT 칼럼명4 = 비교값4 
  AND NOT 칼럼명5 > 비교값5;
  ```

<br>

### 연산자 우선순위

- 1순위 : 괄호 ()
- 2순위 : NOT
- 3순위 : 비교 연산자, SQL
- 4순위 : AND
- 5순위 : OR

<br>

## SQLite Aggregate Functions

> Aggregate functions (집계 함수)

- 값 집합에 대한 계산을 수행하고 **단일 값**을 반환
  - 여러 행으로부터 **하나의 결괏값을 반환**하는 함수
- `SELECT` 구문에서만 사용됨
- 예시
  - 테이블 전체 행 수를 구하는 `COUNT(*)`
  - age 컬럼 전체 평균 값을 구하는 `AVG(age)`

<br>

#### `COUNT`

- 그룹의 항목 수를 가져옴, 레코드의 개수 조회

  ```sql
  SELECT COUNT(컬럼) FROM 테이블이름;
  SELECT COUNT(*) FROM users;
  ```

####  `AVG`

- 모든 값의 평균을 계산

#### `MAX`

- 그룹에 있는 모든 값의 최대값을 가져옴

#### `MIN`

- 그룹에 있는 모든 값의 최소값을 가져옴

#### `SUM`

- 모든 값의 합을 계산

> `AVG`, `SUM`, `MIN`, `MAX` 함수들은 기본적으로 해당 컬럼이 **숫자(INTEGER)** 일 때만 사용 가능

```sql
SELECT AVG(컬럼) FROM 테이블이름; 
SELECT SUM(컬럼) FROM 테이블이름; 
SELECT MIN(컬럼) FROM 테이블이름; 
SELECT MAX(컬럼) FROM 테이블이름;
```

<br>

## LIKE

- 패턴 일치를 기반으로 데이터를 조회하는 방법

- SQLite는 패턴 구성을 위한 2개의 `wildcards`를 제공

  - `% (percent sign)`
    - 0개 이상의 문자
  - `_ (underscore)`
    - 임의의 단일 문자

- LIKE statement : 패턴을 확인하여 해당하는 값을 조회하기

  ```sql
  SELECT * FROM 테이블이름 WHERE 컬럼 LIKE '패턴';
  ```

<br>

### wildcards

#### `%` (percent sign)

- 이 자리에 문자열이 있을 수도, 없을 수도 있다.

#### `_` (underscore)

- 반드시 이 자리에 한 개의 문자가 존재해야 한다.

#### wildcards 사용 예시

- `2%` : 2로 시작하는 값

- `%2` : 2로 끝나는 값
- `%2%` : 2가 들어가는 값
- `_2%` : 아무 값이 하나 있고 두 번째가 2로 시작하는 값
- `1___` : 1로 시작하고 총 4자리인 값
- `2_%_% / 2__%` : 2로 시작하고 적어도 3자리인 값

<br>

## ORDER BY

- 조회 결과 집합을 정렬

- `SELECT` 문에 추가하여 사용

- 정렬 순서를 위한 2개의 keyword 제공

  - `ASC` – 오름차순 (**default**)
  - `DESC` - 내림차순

  ```sql
  SELECT * FROM 테이블이름 ORDER BY 컬럼 ASC; 
  SELECT * FROM 테이블이름 ORDER BY 컬럼 DESC;
  ```

<br>

### 예시

```sql
-- SQLite

-- 테이블 생성
-- 정호,유,40,전라북도,016-7280-2855,370
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

-- 데이터를 추가
.mode csv
-- 같은 디렉토리에 있는 users.csv 파일을 users 테이블로
.import users.csv users


-- 쿼리

-- 30세 이상인 사람들
SELECT * FROM users WHERE age >= 30;
-- 30세 이상인 사람들의 이름
SELECT first_name FROM users WHERE age >= 30;
-- 30세 이상인 사람들의 이름 3명만
SELECT first_name FROM users WHERE age >= 30 LIMIT 3;
-- 30세 이상이고 성이 김인 사람
SELECT age, first_name FROM users WHERE age >= 30 AND last_name = '김';

-- 30세 이상인 사람들의 숫자
SELECT COUNT(*) FROM users WHERE age >= 30;
-- 전체 중에 가장 작은 나이
SELECT MIN(age) FROM users;
-- 이씨 중에 가장 작은 나이
SELECT MIN(age) FROM users WHERE last_name = '이';
-- 이씨 중에 가장 작은 나이를 가진 사람의 이름과 계좌잔고
SELECT MIN(age), first_name, balance FROM users WHERE last_name = '이';
-- 30세 이상인 사람들의 평균 나이
SELECT AVG(age) FROM users WHERE age >= 30;
-- 계좌 잔액이 가장 높은 사람
SELECT MAX(balance), first_name FROM users;

-- 지역번호가 02인 사람
SELECT COUNT(*) FROM users WHERE phone LIKE '02-%';
-- 준으로 끝나는 사람
SELECT COUNT(*) FROM users WHERE first_name LIKE '%준';
-- 중간번호가 5114
SELECT COUNT(*) FROM users WHERE phone LIKE '%-5114-%';

-- 나이 오름차순 
SELECT first_name FROM users ORDER BY age ASC LIMIT 10;
-- 나이, 성 순으로 오름차순
SELECT * FROM users ORDER BY age, last_name LIMIT 10;
-- 계좌 잔액 순 내림차순 
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC LIMIT 10;
-- 계좌 잔액 내림차순(높은->낮은 것), 성 오름차순(ㄱ->ㅎ)
SELECT last_name, first_name, balance FROM users ORDER BY balance DESC, last_name ASC LIMIT 10;
```