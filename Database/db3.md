# ✏️ 기본 함수와 연산

### 문자열 함수

- `SUBSTR(문자열, start, length)` : 문자열 자르기
  - 시작 인덱스는 1, 마지막 인덱스는 -1
- `TRIM(문자열)`, `LTRIM(문자열)`, `RTRIM(문자열)` : 문자열 공백 제거
- `LENGTH(문자열)` : 문자열 길이
- `REPLACE(문자열, 패턴, 변경값)` : 패턴에 일치하는 부분을 변경
- `UPPER(문자열)`, `LOWER(문자열)` : 대소문자 변경
- `||` : 문자열 합치기(concatenation)

<br>

### 숫자 함수

- `ABS(숫자)` : 절대값
- `SIGN(숫자)` : 부호 (양수 1, 음수 -1, 0 0)
- `MOD(숫자1, 숫자2) ` : 숫자1을 숫자2로 나눈 나머지
- `CEIL(숫자)`, `FLOOR(숫자)`, `ROUND(숫자, 자리)` : 올림, 내림, 반올림
- `POWER(숫자1, 숫자2)` : 숫자1의 숫자2 제곱
- `SQRT(숫자)` : 제곱근

<br>

### 산술 연산자

- `+`, `-`, `*`, `/` 와 같은 산술 연산자와 우선 순위를 지정하는 `()` 기호를 연산에 활용할 수 있음

  ```sqlite
  SELECT age+1 FROM users;
  ```

<br>

## GROUP BY

### ALIAS

- 칼럼명이나 테이블명이 너무 길거나 다른 명칭으로 확인하고 싶을 때는 ALIAS를 활용

  - 변수처럼 사용 가능

  ```sqlite
  SELECT last_name 성 FROM users;
  SELECT last_name AS 성 FROM users;
  SELECT last_name AS 성 FROM users WHERE 성='김';
  ```

  ```sqlite
  SELECT id, 10000 * weight / (height*height) AS BMI FROM healthcare WHERE smoking = 3 ORDER BY BMI DESC LIMIT 5;
  ```

- `AS` 를 생략하여 공백으로 표현할 수 있음
  - `height, weight AS 키, 몸무게`
  - `height 키, weight 몸무게`
- 별칭에 공백, 특수문자 등이 있는 경우 따옴표로 묶어서 표기

<br>

### `GROUP BY`

- `SELECT `문의 optional 절

- 행 집합에서 요약 행 집합을 만듦

- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦

- **문장에 `WHERE` 절이 포함된 경우 반드시 `WHERE` 절 뒤에 작성해야 함**

  ```sqlite
  SELECT * FROM 테이블이름 GROUP BY 컬럼1, 컬럼2;
  ```

- 지정된 컬럼의 값이 같은 행들로 묶음

- **집계 함수와 활용하였을 때 의미가 있음**

  ```sqlite
  SELECT * FROM users GROUP BY last_name;
  ```

  - 그냥 중복이 제거되었을 뿐 의미가 없다.

  ```sqlite
  SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
  ```

  - 집계 함수를 썼을 때 의미가 있다.

- 그룹화된 각각의 그룹이 **하나의 집합으로 집계 함수의 인수로 넘겨짐**

- `GROUP BY` 절에 명시하지 않은 컬럼은 별도로 지정할 수 없음

  - 그룹마다 하나의 행을 출력하게 되므로 집계 함수 등을 활용해야 함

-  `GROUP BY` 의 결과는 정렬되지 않음

  - 기존의순서와 바뀌는 모습도 있음

  - 원칙적으로 관계형 데이터베이스에서는 `ORDER BY`를 통해 정렬

<br>

### `HAVING`

- 집계 함수는 `WHERE` 절의 조건식에서는 사용할 수 없음 (실행 순서에 의해)

  - `WHERE`로 처리하는 것이 `GROUP BY` 그룹화보다 순서상 앞서 있기 때문

- **집계 결과에서 조건에 맞는 값을 따로 활용하기 위해서 `HAVING`을 활용**

  ```sqlite
  SELECT * FROM 테이블이름 GROUP BY 컬럼1, 컬럼2 HAVING 그룹조건;
  ```

<br>

### SELECT 문장 실행 순서

> FROM => WHERE => GROUP BY => HAVING => SELECT => ORDER BY

1. FROM 테이블을 대상으로
2. WHRE 제약조건에 맞춰서 뽑아서
3. GROUP BY 그룹화한다.
4. HAVING 그룹 중에 조건과 맞는 것 만을
5. SELECT 조회하여
6. ORDER BY 정렬하고
7. LIMIT/OFFSET 특정 위치의 값을 가져온다.

### 작성 순서

```sqlite
SELECT 칼럼명
FROM 테이블명
WHERE 조건식
GROUP BY 칼럼 혹은 표현식 
HAVING 그룹조건식
ORDER BY 칼럼 혹은 표현식 
LIMIT 숫자 OFFSET 숫자;
```

<br>

## ALTER TABLE

- 테이블 이름 변경

  ```sqlite
  ALTER TABLE table_name
  RENAME TO new_name;
  ```

- 새로운 column 추가

  ```sqlite
  ALTER TABLE table_name
  ADD COLUMN column_definition;
  ```

- column 이름 수정

  ```sqlite
  ALTER TABLE table_name
  RENAME COLUMN current_name TO new_name;
  ```

- column 삭제

  ```sqlite
  ALTER TABLE table_name
  DROP COLUMN column_name;
  ```

### 주의

>테이블에 있던 기존 레코드들에는 새로 추가할 필드에 대한 정보가 없다.

- **`NOT NULL` 형태의 컬럼은 추가가 불가능하다.**

```sqlite
ALTER TABLE 테이블이름 ADD COLUMN 컬럼이름 데이터타입설정;
```

```sqlite
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;

-- Error: Cannot add a NOT NULL colmn with default value NULL
```

- **기본 값 (DEFAULT)** 설정하자

  ```sqlite
  ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL DEFAULT '소제목';
  ```

<br>

### 예시

```sqlite
SELECT * FROM users LIMIT 1;

-- pipe sign 엔터 위에 있어요 보통
-- 문자열 합치기 ||
-- (성+이름) 출력, 5명만
SELECT 
    last_name || first_name 이름,
    age,
    country,
    phone,
    balance
FROM users
LIMIT 5;

-- 이름   age  country  phone          balance
-- ---  ---  -------  -------------  -------
-- 유정호  40   전라북도     016-7280-2855  370
-- 이경희  36   경상남도     011-9854-5133  5900
-- 구정자  37   전라남도     011-4177-8170  3100
-- 장미경  40   충청남도     011-9079-4419  250000
-- 차영환  30   충청북도     011-2921-4284  220

-- 문자열 길이 LENGTH
SELECT 
    LENGTH(first_name),
    first_name
FROM users
LIMIT 5;
-- LENGTH(first_name)  first_name
-- ------------------  ----------
-- 2                   정호
-- 2                   경희
-- 2                   정자
-- 2                   미경
-- 2                   영환

-- 문자열 변경 REPLACE
-- 016-7280-2855 => 01672802855
SELECT 
    first_name,
    phone,
    REPLACE(phone, '-', '')
FROM users
LIMIT 5;

-- 숫자 활용
SELECT MOD(5, 2)
FROM users
LIMIT 1;

-- 올림, 내림, 반올림
SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14)
FROM users
LIMIT 1;

-- 9의 제곱근
SELECT SQRT(9)
FROM users
LIMIT 1;

-- 9^2
SELECT POWER(9, 2)
FROM users
LIMIT 1;

-- GROUP BY

-- 성별 갯수
SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name;

-- GROUP BY에서 활용하는 컬럼을 제외하고는
-- 집계함수를 쓰세요.
SELECT last_name, AVG(age), COUNT(*)
FROM users
GROUP BY last_name;

-- 참고...
SELECT last_name, age
FROM users
WHERE last_name = '곽';
-- last_name  age
-- ---------  ---
-- 곽          25
-- 곽          30
-- 곽          28
-- 곽          15

-- GROUP BY는 결과가 정렬되지 않아요. 기존 순서와 바뀜
-- 원칙적으로 내가 정렬해서 보고 싶으면 ORDER BY!

SELECT *
FROM users
LIMIT 5;
-- first_name  last_name  age  country  phone          balance       
-- ----------  ---------  ---  -------  -------------  -------       
-- 정호          유          40   전라북도     016-7280-2855  370    
-- 경희          이          36   경상남도     011-9854-5133  5900   
-- 정자          구          37   전라남도     011-4177-8170  3100   
-- 미경          장          40   충청남도     011-9079-4419  250000 
-- 영환          차          30   충청북도     011-2921-4284  220  

SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name
LIMIT 5;

-- last_name  COUNT(*)
-- ---------  --------
-- 강          23
-- 고          10
-- 곽          4
-- 구          2
-- 권          17

-- GROUP BY WHERE를 쓰고 싶다.
-- 100번 이상 등장한 성만 출력하고 싶음. 
SELECT last_name, COUNT(last_name)
FROM users
WHERE COUNT(last_name) > 100
GROUP BY last_name;
-- 오류 발생!
-- Parse error: misuse of aggregate: COUNT()
--   LECT last_name, COUNT(last_name) FROM users WHERE COUNT(last_name) > 100 GROUP

-- 조건에 따른 GROUP 하시려면
-- HAVING을 쓴다!
SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name) > 100;
```