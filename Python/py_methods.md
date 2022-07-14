# 🗃 데이터 구조 (Data Structure)

함수 (function)

>  input()**.split()** => **문자열.split()**
>
> [1, 2, 3]**.append(4)** => **리스트.append(4)**

`(데이터)타입 . 메서드()`

## 메서드 (methods)

```python
# 리스트 메서드 활용
a = [10, 1, 100]
# 정렬(sort)
new_a = a.sort()
print(a, new_a)
# [1, 10, 100] None
# 리스트 메서드를 활용하면, 그 메서드를 정렬된 상태로 변경(원본 변경)
# return되는 것은 None

# 리스트에 sorted 함수를 활용
a = [10, 1, 100]
# 정렬(sort)
new_b = sorted(b)
print(b, new_b)
#[10, 1, 100] [1, 10, 100]
# sorted 함수를 활용하면, 원본을 변경하지 않음
# return되는 것은 정렬된 리스트

# 실제 활용 코드
a = [10, 1, 100]
a.sort()
# a를 정렬된 상태로 활용

b = [10, 1, 100]
b = sorted(b)
# b를 정렬된 상태로 활용
```

## 시퀀스 (순서가 있는 데이터 구조)

## 문자열(String Type)

### 문자열 탐색/검증

| 문법         | 설명                                                         |
| ------------ | ------------------------------------------------------------ |
| s.find(x)    | x의 첫 번째 위치를 반환. 없으면, -1을 반환                   |
| s.index(x)   | x의 첫 번째 위치를 반환. 없으면, 오류 발생                   |
| s.isalpha()  | 알파벳 문자 여부, 단순 알파벳이 아닌 유니코드 상 Letter (한국어도 포함) |
| s.isupper()  | 대문자 여부                                                  |
| s.islower()  | 소문자 여부                                                  |
| s.istitile() | 타이틀 형식 여부                                             |

#### 문자열 탐색

- `.find(x)`
  
  - x의 첫 번째 위치를 반환. 없으면, -1을 반환함.
  
  ```python
  print('apple'.find('p')) # 1 
  print('apple'.find('k')) # -1
  ```
  
- `.index(x)`
  - x의 첫 번째 위치를 반환. 없으면, 오류 발생
  
  ```python
  print('apple'.index('p’))
  # 1
  'apple'.index('k')
  # -------------------------------------------
  # ValueError Traceback (most recent call last)
  # ----> 1 'apple'.index('k')
  # ValueError: substring not found
  ```

#### 문자열 관련 검증 메소드

```python
print('abc'.isalpha()) # True 
print('Ab'.isupper()) # False 
print('ab'.islower()) # True
print('Title Title!'.istitle()) # True

# 알파벳인지 검증
.isupper() # 대문자?
# 앞에가 대문자인 것을 타이틀
```



숫자인지 검증하려면 `isdecimal()` 쓰기

### 문자열 변경

- `.replace(old, new[,count])`
  - **바꿀 문자 반환**
  - count를 지정하면, 해당 개수만큼만 시행, 선택 사항
- `.strip([chars])`
- 특정한 문자들을 지정하면,
- **양쪽을 제거하거나(`strip`)**, 왼쪽을 제거하거나
- **문자열을 지정하지 않으면 공백을 제거함(space, \n)**

- .split(sep = None, maxsplit = -1)
  - 문자열을 특정한 단위로 나눠 **리스트로 반환**
- 'separator.join'
  - 반복가능한(iterable) 컨테이너 요소들을 separator(구분자)로 합쳐 **문자열 반환**
    - **iterable에 문자열이 아닌 값이 있으면 TypeError 발생**

```python
names = ','.join(['홍길동', '김철수'])
print(names)
# 홍길동, 김철수

numbers = ' '.join([10, 20, 100])
print(numbers)
# TypeError: sequence item 0: expected str instance, int found

numbers = ' '.join(map(str,[10, 20, 100]))
# 10 20 100
```

### 기타 변경

문자열은 스스로 바뀌는 경우 x inmutable이기 때문에(튜플 레인지)

모두 바뀐 결과를 반환한다.

replace

-strip-

split

separator

많이씀!!

## 리스트 (list)

변경 가능(mutable)

append

pop

sort

count

많이 씀!

insert remove도 씀

### 값 추가 및 삭제

- **.append(x)**

  - 리스트의 맨 뒤에 추가됨

- .extend (iterable)

  - 리스트에 iterable의 항목을 추가함

  - 반드시 리스트로 하나로 묶어야함

  - 문자열을 input하면 단어 하나하나 반환

    ```python
    a = ['apple']
    a.extend
    ```

    

- .insert(i,x)

  - 정해진 위치 i에 값을 추가함
  - 인덱스 i에 추가

- .remove(x)

  - 리스트에서 
  - 값을 제거

- .pop(x)

  - 정해진 위치 i 값 삭제

- .clear()

### 탐색 및 정렬

- .index(x)
  - x값을 찾아 해당 index 값을 반환
- .count(x)
  - 원하는 값의 개수를 반환함
- .sort()
  - 원본 리스트를 정렬함. None 반환
  - sorted 함수와 비교할 것
- .reverse()
  - 순서를 반대로 뒤집음 (정렬하는 것이 아님). None 반환

```python
a = [1, 2, 3]
a = a.append(4)
print(a)
# None


a.append(4)
print(a)
```

```python
# 리스트는 mutable
a = [1, 2, 3]
a[0] = 100
prnit(a)
#[100, 2, 3]

# 문자열은 immutable
# 문자열의 첫번째 인덱스에 해당하는 값을 바꿀 수 없다.
a = 'hi'
a[0] = 'c'
print(a)
# TypeError: 'str' object does not support item assignment
```

```python

['1','2','3'].index('2')+10
```

## 컬렉션

### 세트 메서드

## 딕셔너리

### 조회

- .get(key)
  - key를 통해 value를 가져옴
- default 값을 설정 -> 0
- .pop
  - key가 딕셔너리에 있으면 제거하고 해당 값을 반환
  - 그렇지 않으면 default를 반환
  - default값이 없으면 KeyError
- .update
  - 값을 제공하는 key, va

```python
# 기본 순회
# key가 기준이고, 직접 딕셔너리에 key로 접근하면 value를 얻을 수 있다.

# 다양한 방법 => 일종의 리스트, 안에는 문자열
items
# 일종의 리스트안에 tuple!

# value 값 1 더하기
my_dict_3 = {'a': 0}

```

python tuter

[1, 2, 3] + [4, 5] = [1, 2, 3, 4, 5]

{'a': 'apple'} + {'b': 'banana'} = Error