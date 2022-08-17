# 🏢 Database

- 데이터베이스는 **체계화된 데이터**의 모임
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된 (하나 이상의) 자료의 모음으로 그 내용을 고도로 구조화 함으로써 검색과 갱신의 효율화를 꾀한 것
- 즉, **몇 개의 자료 파일을 조직적으로 통합**하여 **자료 항목의 중복을 없애**고 **자료를 구조화하여 기**억시켜 놓은 **자료의 집합체**

<br>

### 데이터베이스로 얻는 장점들

- 데이터 중복 최소화
- 데이터 무결성 (정확한 정보를 보장)
- 데이터 일관성
- 데이터 독립성 (물리적 / 논리적)
- 데이터 표준화
- 데이터 보안 유지

<br>

## RDB

> 관계형 데이터베이스 (Relational Database)

- 서로 관련된 데이터를 저장하고 접근할 수 있는 데이터베이스 유형

- 키(key)와 값(value)들의 간단한 관계(relation)를 표(table) 형태로 정리한 데이터베이스

  | 고유 번호 |  이름  | 주소 | 나이 |
  | :-------: | :----: | :--: | :--: |
  |     1     | 홍길동 | 제주 |  20  |
  |     2     | 김길동 | 서울 |  30  |
  |     3     | 박길동 | 독도 |  40  |

<br>

- `스키마(schema)` 

  데이터베이스에서 자료의 구조, 표현방법, 관계등 전반적인 **명세를 기술**한 것

  | column  | datatype |
  | :-----: | :------: |
  |   id    |   INT    |
  |  name   |   TEXT   |
  | address |   TEXT   |
  |   age   |   INT    |

- `테이블(table)`

  열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합

- `열(column)`

  각 열에 고유한 데이터 형식 지정

  - 아래의 예시에서는 name이란 필드에 고객의 이름(TEXT) 정보가 저장

  |  id  |  name  | address | age  |
  | :--: | :----: | :-----: | :--: |
  |  1   | 홍길동 |  제주   |  20  |
  |  2   | 김길동 |  서울   |  30  |
  |  3   | 박길동 |  독도   |  40  |

- `행(row)`

  실제 데이터가 저장되는 형태

- `기본키(Primary Key)`

  **각 행(레코드)의 고유 값**

  - 반드시 설정해야 하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용 됨
    - 절대 중복되어선 안됨.

## RDBMS

> 관계형 데이터베이스 관리 시스템 (RDBMS)
>
> - 관계형 모델을 기반으로 하는 데이터베이스 관리시스템을 의미

### SQLite

- 서버 형태가 아닌 **파일 형식**으로 응용 프로그램에 넣어서 사용하는 **비교적 가벼운 데이터베이스**
- 구글 안드로이드 운영체제에 기본적으로 탑재된 데이터베이스이며, 임베디드 소프트웨어에도 많이 활용됨
- 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이기 때문에 자유롭게 사용가능

<br>

#### SQLite Data Type

1. NULL
2. INTEGER
   - 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트에 저장된 부호 있는 정수 
3. REAL
   - 8바이트 부동 소수점 숫자로 저장된 부동 소수점 값 

4. TEXT

5. BLOB
   - 입력된 그대로 정확히 저장된 데이터 (별다른 타입 없이 그대로 저장)

<br>

#### Sqlite Type Affinity (1/2)

- 특정 컬럼에 저장하도록 권장하는 데이터 타입 

1. INTEGER

2. TEXT

3. BLOB

4. REAL

5. NUMERIC

<br>

## SQL (Structured Query Language)

>  관계형 데이터베이스 관리시스템의 **데이터 관리** 를 위해 **특수 목적으로 설계된 프로그래밍 언어** 

- 데이터베이스 스키마 생성 및 수정
- 자료의 검색 및 관리
- 데이터베이스 객체 접근 조정 관리

|                        분류                         |                             개념                             |              예시              |
| :-------------------------------------------------: | :----------------------------------------------------------: | :----------------------------: |
|  DDL - 데이터 정의 언어 (Data Definition Language)  | 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 |       CREATE DROP ALTER        |
| DML - 데이터 조작 언어 (Data Manipulation Language) |    데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어     |  INSERT SELECT UPDATE DELETE   |
|   DCL - 데이터 제어 언어 (Data Control Language)    |    데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어    | GRANT  REVOKE  COMMIT ROLLBACK |

<br>

### SQL Keywords - Data Manipulation Language

- `INSERT` : 새로운 데이터 삽입(추가)
- `SELECT` : 저장되어있는 데이터 조회
- `UPDATE` : 저장되어있는 데이터 갱신
- `DELETE` : 저장되어있는 데이터 삭제

<br>

## 테이블 생성 및 삭제

#### SQLite3 실행하기

```sqlite
sqlite3
```

#### 특정 데이터베이스 실행하기

```sqlite
sqlite3 tutorial.sqlite3
```

<br>

### 데이터베이스 생성하기

```sqlite
.database
```

### csv 파일을 table로 만들기

```sqlite
.mode csv
.import (csv명).csv (테이블 명)
.tables
```

### SELECT 확인하기

```sqlite
SELECT * FROM (테이블 명)
```

- SELECT 문은 특정 테이블의 레코드(행) 정보를 반환한다.
- `*`은 '모든'이라는 의미를 가짐

<br>

#### 터미널 view 변경하기

```sqlite
.headers on
.mode column
```

<br>

### 테이블 생성

```sqlite
CREATE TABLE (테이블 명) (
  (열) (데이터 타입) (제약 조건)
);
```

### 테이블 확인

```sqlite
.tables
```

### 특정 테이블의 schema 조회

```sqlite
.schema (테이블 명)
```

### 테이블 삭제

```sqlite
DROP TABLE (테이블 명);
```

<br>

#### 기타

- 주석 : `--`

- 문장마다 세미콜론(`;`)을 붙여야함
- `*`은 전체 조회를 뜻함

<br>

### 필드제약조건

- `NOTNULL` : NULL 값 입력 금지
- `UNIQUE` : 중복 값 입력 금지 (NULL 값은 중복 입력 가능)
- `PRIMARYKEY` : 테이블에서 반드시 하나. `NOTNULL`+`UNIQUE `
- `FOREIGN KEY` : 외래키. 다른 테이블의 Key
- `CHECK` : 조건으로 설정된 값만 입력 허용
- `DEFAULT` : 기본 설정 값

<br>

## CRUD

> CREATE, READ, UPDATE, DELETE

<br>

### CREATE

#### `INSERT`

- 테이블에 단일 행 삽입

  ```sqlite
  INSERT INTO 테이블_이름 (컬럼1, 컬럼2) VALUES (값1, 값2);
  ```

- 테이블에 정의된 모든 컬럼에 맞춰 순서대로 입력

  ```sqlite
  INSERT INTO 테이블_이름 VALUES (값1, 값2, 값3);
  ```

- **rowid :** SQLite에서 PRIMARY KEY가 없는 경우 자동으로 증가하는 PK 컬럼

  - schema에 id를 직접 작성했을 때, 입력할 column들을 명시하지 않으면 자동으로 입력되지 않음

  - 첫번째 방법

    ```sqlite
    INSERT INTO classmates VALUES (1,'홍길동',30,'서울');
    ```

    - id를 포함한 모든 value를 작성

  - 두번째 방법

    ```sqlite
    INSERT INTO classmates (name, age, address) VALUES ('홍길동',30,'서울');
    ```

    - 각 value에 맞는 column들을 명시적으로 작성

<br>

### READ

#### `SELECT`

- 테이블에서 데이터를 조회
- SELECT 문은 SQLite에서 가장 기본이 되는 문이며 다양한 절(clause)와 함께 사용
  - `ORDER BY`, `DISTINCT`, `WHERE`, `LIMIT`, `GROUP BY` ...

#### `LIMIT`

- 쿼리에서 반환되는 행 수를 제한

- 특정 행부터 시작해서 조회하기 위해 `OFFSET` 키워드와 함께 사용하기도 함

  ```sqlite
  SELECT 컬럼1, 컬럼2 ... FROM 테이블명 LIMIT 숫자;
  ```

#### `WHERE`

- 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정

#### `SELECT DISTINCT`

- 조회 결과에서 중복 행을 제거
- `DISTINCT` 절은 `SELECT` 키워드 **바로 뒤에** 작성해야 함

#### `OFFSET`

- 처음부터 주어진 요소나 지점까지의 차이를 나타내는 정수형

  - 문자열 'abced'’ 에서 문자 'c'는 시작점 'a'에서 2의 OFFSET을 지님

  ```sqlite
  SELECT * FROM MY_TABLE LIMIT 10 OFFSET 5
  ```

  - 6번째 행 부터 10개 행을 조회 (6번째 행부터 10개를 출력)
  - 0 부터 시작함

  ```sqlite
  SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
  ```

  - 2칸 뛰고 첫번째 값 => 3번째 값 출력

<br>

### DELETE

- 테이블에서 행을 제거

- 데이터 삭제

  ```sqlite
  DELETE FROM 테이블 이름 WHERE 조건;
  ```

  - 중복 불가능한(UNIQUE) 값인 rowid를 기준으로 삭제하기

  ```sqlite
  DELETE FROM classmates WHERE rowid = 5;
  ```

- `drop`은 다 지우는 것

- `delete`는 레코드 하나를 지우는 것

#### `AUTOINCREMENT`

- SQLite가 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지

```sqlite
CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
INSERT INTO students VALUES 
(1, '홍길동'),
(2, '김철수'),
(3, '이호영'),
(4, '박민희'), 
(5, '최혜영');

DELETE FROM members WHERE rowid=5;
INSERT INTO members (name) VALUES ('이민호');
SELECT * FROM members;
id name
-- ----
1 홍길동
2 김철수
3 이호영
4 박민희
6 이민호
```

<br>

### UPDATE

- 기존 행의 데이터를 수정

- **SET** clause에서 테이블의 각 열에 대해 새로운 값을 설정

  ```sqlite
  UPDATE 테이블 이름 SET 컬럼1=값1, 컬럼2=값2,... WHERE 조건;
  ```
