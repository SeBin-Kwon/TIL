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
print('Title Title!'.istitle()) # True 앞에가 대문자인 것이 타이틀

# 알파벳인지 검증
.isupper() # 대문자?
```

- `.isdecimal()` ⊆ `.isdigit()` ⊆ `.isnumeric()`
  - 숫자인지 검증하려면 .`isdecimal()` 쓰기

### 문자열 변경

| 문법                                 | 설명                                       |
| ------------------------------------ | ------------------------------------------ |
| **s.replace(*old, new[,count]*)**    | 바꿀 대상 글자를 새로운 글자로 바꿔서 반환 |
| **s.strip(*[chars]*)**               | 공백이나 특정 문자를 제거                  |
| **s.split(*sep=None, maxsplit=-1*)** | 공백이나 특정 문자를 기준으로 분리         |
| **'*separator*'.join(*[iterable]*)** | 구분자로 iterable을 합침                   |
| s.capitalize()                       | 가장 첫 번째 글자를 대문자로 변경          |
| s.title()                            | '나 공백 이후를 대문자로 변경              |
| s.upper()                            | 모두 대문자로 변경                         |
| s.lower()                            | 모두 소문자로 변경                         |
| s.swapcase()                         | 대↔ 소문자 서로 변경                       |

- `.replace(old, new[,count])`

  - **바꿀 대상 글자를 새로운 글자로 바꿔서 반환**
  - count를 지정하면, 해당 개수만큼만 시행, 선택 사항

  ```python
  print('coone'.replace('o', 'a')) # caane
  print('wooooowoo'.replace('o', '!', 2)) # w!!ooowoo
  ```

- `.strip([chars])`

  - 특정한 문자들을 지정하면,
  - **양쪽을 제거하거나(`strip`)**, 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(rstrip)
    - **문자열을 지정하지 않으면 공백을 제거함(`space`, `\n`)**


  ```python
  print(' 와우!\n'.strip()) # '와우!'
  print(' 와우!\n'.lstrip()) # '와우!\n'
  print(' 와우!\n'.rstrip()) # ' 와우!'
  print('안녕하세요????'.rstrip('?')) # '안녕하세요'
  ```

- `.split(sep = None, maxsplit = -1)`

  - 문자열을 특정한 단위로 나눠 **리스트로 반환**
    - `sep`이 `None`이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주하고, 선행/후행 공백은 빈 문자열에 포함시키지 않음.
    - `maxsplit`이`-1`인경우에는제한이없음.

  ```python
  print('a,b,c'.split('_')) # ['a,b,c']
  print('a b c'.split()) # ['a', 'b', 'c']
  ```

- `'separator'.join([iterable])`

  - 반복가능한(iterable) 컨테이너 요소들을 separator(구분자)로 합쳐 **문자열 반환**
    - **iterable에 문자열이 아닌 값이 있으면 TypeError 발생**

  ```python
  print(''.join(['3', '5'])) # 35
  ```

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

- 문자열 변경 예시

  ```python
  msg = 'hI! Everyone.'
  print(msg) # hI! Everyone.
  print(msg.capitalize()) # Hi! everyone.
  print(msg.title()) # Hi! Everyone.
  print(msg.upper()) # HI! EVERYONE.
  print(msg.lower()) # hi! everyone.
  print(msg.swapcase()) # Hi! eVERYONE.
  ```

  - 문자열은 `inmutable`이기 때문에(ex: 튜플, 레인지) 스스로 바뀌는 경우가 없다.

    모두 바뀐 결과를 반환한다.

## 리스트 (list)

- 변경 가능한 값들의 나열된 자료형
- 순서를 가지며, 서로 다른 타입의 요소를 가질 수 있음

- **변경 가능하며(mutable)**, 반복 가능함(iterable)
- 항상 대괄호 형태로 정의하며, 요소는 콤마로 구분 `[ 0,1,2,3,4,5 ]`

| 문법                   | 설명                                                         |
| ---------------------- | ------------------------------------------------------------ |
| **L.append(x)**        | 리스트 마지막에 항목 x를 추가                                |
| **L.insert(i, x)**     | 리스트 인덱스 i에 항목 x를 삽입                              |
| **L.remove(x)**        | 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거, 항목이 존재하지 않을 경우, ValueError |
| **L.pop()**            | 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거        |
| **L.pop(i)**           | 리스트의 인덱스 i에 있는 항목을 반환 후 제거                 |
| L.extend(m)            | 순회형 m의 모든 항목들의 리스트 끝에 추가 (+=과 같은 기능)   |
| L.index(x, start, end) | 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환 |
| L.reverse()            | 리스트를 거꾸로 정렬                                         |
| **L.sort()**           | 리스트를 정렬 (매개변수 이용가능)                            |
| **L.count(x)**         | 리스트에서 항목 x가 몇 개 존재하는지 갯수를 반환             |

### 값 추가 및 삭제

- **`.append(x)`**

  - 리스트에 값을 추가함 (맨 뒤에 추가됨)

  ```python
  cafe = ['starbucks', 'tomntoms', 'hollys'] print(cafe)
  # ['starbucks', 'tomntoms', 'hollys'] cafe.append('banapresso')
  print(cafe)
  # ['starbucks', 'tomntoms', 'hollys', 'banapresso']
  ```

```python
a = [1, 2, 3]
a = a.append(4)
print(a) # None
# a.append(4)의 return 값을 a에 저장한다.
# 리스트.append()의 메서드는 반환값이 None임!

a = [1, 2, 3]
a.append(4) 
print(a) # [1, 2, 3, 4]
```

- `.extend (iterable)`

  - 리스트에 `iterable`의 항목을 추가함

  - 반드시 리스트로 하나로 묶어야함

  - 문자열을 `input`하면 단어 하나하나 반환


  ```python
  cafe = ['starbucks', 'tomntoms', 'hollys']
  print(cafe)
  # ['starbucks', 'tomntoms', 'hollys']
  cafe.extend(['cafe', 'test'])
  print(cafe)
  # ['starbucks', 'tomntoms', 'hollys', 'cafe', 'test]
  
  a = ['apple']
  a.extend(['banana', 'mango'])
  print(a) 
  # ['apple', 'banana', 'mango']
  
  a.extend('banana')
  print(a)
  # ['apple', 'banana', 'mango', 'b', 'a', 'n', 'a', 'n', 'a']
  ```

- `.insert(i,x)`

  - 정해진 위치 i에 값을 추가함

  ```python
  cafe = ['starbucks', 'tomntoms'] 
  print(cafe)
  # ['starbucks', 'tomntoms'] 
  cafe.insert(0, 'start') 
  print(cafe)
  # ['start', 'starbucks', 'tomntoms']
  
  cafe = ['starbucks', 'tomntoms']
  print(cafe)
  # ['starbucks', 'tomntoms']
  cafe.insert(10000, 'end') # 리스트 길이보다 큰 경우 맨 뒤에 추가함
  print(cafe)
  # ['starbucks', 'tomntoms', 'end']
  ```

- `.remove(x)`

  - 리스트에서 값이 x인 것 삭제

  ```python
  numbers = [1, 2, 3, 'hi'] 
  print(numbers) # [1, 2, 3, 'hi'] 
  numbers.remove('hi') 
  print(numbers) # [1, 2, 3]
  
  numbers.remove('hi') # 없는 경우 ValueError
  # ----------------
  # ValueError Traceback (most recent call last) # ----> 1 numbers.remove('hi')
  # ValueError: list.remove(x): x not in list
  ```

- `.pop(i)`

  - 정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환함
  - i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함

  ```python
  numbers = ['hi', 1, 2, 3] 
  # ['hi', 1, 2, 3] 
  pop_number = numbers.pop() 
  print(pop_number)
  #3
  print(numbers)
  # ['hi', 1, 2]
  
  numbers = ['hi', 1, 2, 3] 
  # ['hi', 1, 2, 3] 
  pop_number = numbers.pop(0) 
  print(pop_number)
  # 'hi'
  print(numbers)
  # [1, 2, 3]
  ```

- `.clear()`

  - 모든 항목을 삭제함

  ```python
  numbers = [1, 2, 3] 
  print(numbers)
  # [1, 2, 3] 
  print(numbers.clear()) 
  # []
  ```

### 탐색 및 정렬

- `.index(x)`

  - x값을 찾아 해당 index 값을 반환

  ```python
  numbers = [1, 2, 3, 4] 
  print(numbers) # [1, 2, 3, 4] 
  print(numbers.index(3)) # 2
  print(numbers.index(100)) # 없는 경우 ValueError
  # ---------------------
  # ValueError Traceback (most recent call last)
  #       2 print(numbers)
  # 3 print(numbers.index(3)) 
  # ----> 4 print(numbers.index(100))
  # ValueError: 100 is not in list
  ```

- `.count(x)`

  - 원하는 값의 개수를 반환함

  ```python
  numbers = [1, 2, 3, 1, 1] 
  print(numbers.count(1)) # 3 
  print(numbers.count(100)) # 0
  ```

- `.sort()`

  - 원본 리스트를 정렬함. None 반환
  - `sorted` 함수와 비교할 것

  ```python
  numbers = [3, 2, 5, 1]
  result = numbers.sort() 
  print(numbers, result) 
  # [1, 2, 3, 5] None
  # 원본 변경
  
  numbers = [3, 2, 5, 1] 
  result = sorted(numbers) 
  print(numbers, result)
  # [3, 2, 5, 1] [1, 2, 3, 5]
  # 정렬된 리스트를 반환. 원본 변경 없음

- `.reverse()`

  - 순서를 반대로 뒤집음 (정렬하는 것이 아님). None 반환

  ```python
  numbers = [3, 2, 5, 1] 
  result = numbers.reverse() 
  print(numbers, result)
  # [1, 5, 2, 3] None
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
a = [1, 2, 3]
# sum(a)의 결과(int, 합 계산 결과)를 result 할당
result = sum(a) # 6

numbers = [1, 3, 2]
result = numbers.reverse() # None이 반환되고, numbers는 바뀌어있음
# 그래서 일반적으로 코드는
numbers.reverse()

a = ['1','2','3'].index('2')+10
print(a) # 11
# .index의 '2'는 a리스트의 인덱스 [1]에 해당하므로 값이 1이다.
# 1 + 10 = 11
```



## 컬렉션 (순서가 없는 데이터 구조)

## 세트 (set)

- 유일한 값들의 모음(collection)
- 순서가 없고 중복된 값이 없음.
  - 수학에서의 집합과 동일한 구조를 가지며, 집합 연산도 가능
- 변경 가능하며(mutable), 반복 가능함(iterable)
  - 단, 세트는 순서가 없어 반복의 결과가 정의한 순서와 다를 수 있음

### 세트 메서드

| 문법            | 설명                                                         |
| --------------- | ------------------------------------------------------------ |
| s.copy()        | 세트의 얕은 복사본을 반환                                    |
| s.add(x)        | 항목 x가 세트 s에 없다면 추가                                |
| s.pop()         | 세트s에서 랜덤하게 항목을 반환하고 해당 항목을 제거, 세트가 비어 있을 경우, KeyError |
| s.remove(s)     | 항목 x를 세트 s에서 삭제, 항목이 존재하지 않을 경우, KeyError |
| s.discard(x)    | 항목 x가 세트 s에 있는 경우, 항목 x를 세트s에서 삭제         |
| s.update(t)     | 세트 t에 있는 모든 항목 중 세트 s에 없는 항목을 추가         |
| s.clear()       | 모든 항목을 제거                                             |
| s.isdisjoint(t) | 세트 s가 세트 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True반환 |
| s.issubset(t)   | 세트 s가 세트 t의 하위 세트인 경우, True반환                 |
| s.issuperset(t) | 세트 s가 세트 t의 상위 세트인 경우, True반환                 |



## 딕셔너리 (Dictionary)

- 키-값(key-value) 쌍으로 이뤄진 모음(collection)

  - 키(key)
    - 불변 자료형만 가능 (리스트, 딕셔너리 등은 불가능함)
  - 값(values)
    - 어떠한형태든관계없음

- 키와 값은 `:` 로 구분됩니다. 개별 요소는 `,` 로 구분됩니다.

- 변경 가능하며(mutable), 반복 가능함(iterable)

  - 딕셔너리는 반복하면 키가 반환됩니다.

  ```python
  students = {'홍길동': 30, '김철수': 25} 
  students['홍길동'] # 30
  ```

| 문법                | 설명                                                         |
| ------------------- | ------------------------------------------------------------ |
| d.clear()           | 모든 항목을 제거                                             |
| d.keys()            | 딕셔너리 d의 모든 키를 담은 뷰를 반환                        |
| d.values()          | 딕셔너리 d의 모든 값를 담은 뷰를 반환                        |
| d.items()           | 딕셔너리 d의 모든 키-값의 쌍을 담은 뷰를 반환                |
| d.get(k)            | 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 None을 반환 |
| d.get(k, v)         | 키 k의 값을 반환하는데, 키 k가 딕셔너리 d에 없을 경우 v을 반환 |
| d.pop(k)            | 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데, 키 k가 딕셔너리 d에 없을 경우 KeyError를 발생 |
| d.pop(k, v)         | 키 k의 값을 반환하고 키 k인 항목을 딕셔너리 d에서 삭제하는데, 키 k가 딕셔너리 d에 없을 경우 v를 반환 |
| d.update([*other*]) | 딕셔너리 d의 값을 매핑하여 업데이트                          |

### 조회

- `.get(key)`

  - key를 통해 value를 가져옴
  - KeyError가 발생하지 않으며, default 값을 설정할 수 있음(기본: None)

  ```python
  my_dict = {'apple': '사과', 'banana': '바나나'}
  my_dict['pineapple']
  # ------------------------------
  # KeyError Traceback (most recent call last) # 1 my_dict = {'apple': '사과', 'banana': '바나나'}
  # ----> 2 my_dict['pineapple’]
  # KeyError: 'pineapple'
  
  my_dict = {'apple': '사과', 'banana': '바나나'} print(my_dict.get('pineapple'))
  # None
  print(my_dict.get('apple'))
  # 사과 
  print(my_dict.get('pineapple', 0)) 
  #0 정보는 없지만 조작하고 싶을 때 디폴트 값을 설정해놓을 수 있다.
  ```

- `.pop(key[,default])`

  - key가 딕셔너리에 있으면 제거하고 해당 값을 반환
  - 그렇지 않으면 default를 반환
  - default값이 없으면 KeyError

  ```python
  my_dict = {'apple': '사과', 'banana': '바나나'} 
  data = my_dict.pop('apple')
  print(data, my_dict)
  # 사과 {'banana': '바나나'}
  
  my_dict = {'apple': '사과', 'banana': '바나나'} 
  data = my_dict.pop('pineapple')
  print(data, my_dict)
  # ----------------
  # KeyError Traceback (most recent call last)
  # 1 my_dict = {'apple': '사과', 'banana': '바나나'} # ----> 2 data = my_dict.pop('pineapple')
  # 3 print(data, my_dict)
  # KeyError: 'pineapple'
  ```

- `.update([other])`

  - 값을 제공하는 key, value로 덮어씁니다.

  ```python
  my_dict = {'apple': '사', 'banana': '바나나'} my_dict.update(apple='사과')
  print(my_dict)
  # {‘apple’: ‘사과’, 'banana': '바나나'}
  ```

```python
# 기본 순회

my_dict = {'apple': '사과', 'banana': '바나나'}
# key가 기준이고, 직접 딕셔너리에 key로 접근하면 value를 얻을 수 있다!
for word in my_dict:
    print(word, my_dict[word]) # apple 사과 # banana 바나나

# 다양한 방법
print(my_dict.keys(), type(my_dict.keys()))
# dict_keys(['apple', 'banana']) 
# 타입 : dict_keys(일종의 리스트)

print(my_dict.values())
# dict_values(['사과', '바나나'])(일종의 리스트)

# 응용
for value in my_dict.values():
    print(value) # 사과 # 바나나

print(my_dict.items())
# 일종의 리스트안에, tuple!
# dict_items([('apple', '사과'), ('banana', '바나나')])
for k, v in my_dict.items():
    print(k, v)
# apple 사과 # banana 바나나

# 딕셔너리에 값 추가하기
my_dict_2 = {}
my_dict_2['a'] = 'airplane'

# 1 증가 시키기
my_dict_3 = {'a': 0}
my_dict_3['a'] += 1 
# 키값 'a'에 접근하여 밸류 0과 1을 더해 'a'에 할당
print(my_dict_3)
# {'a' : 1 }

my_list = [10, 11, 12]
my_list[0] = my_list[0] + 1
# 인덱스[0](첫번째)에 접근해 1을 더한 것을 인덱스[0]에 할당 

my_dict = {'apple': '사과', 'banana': '바나나'}
print(my_dict['apple']) # 사과

for word in my_dict: # 'apple', 'banana' 키값이 나옴
    print(my_dict[word]) # 사과 , 바나나 
    # 딕셔너리에 키값을 넣어 직접 접근하여 밸류를 얻음
    
[1, 2, 3] + [4, 5] 
# [1, 2, 3, 4, 5]
{'a': 'apple'} + {'b': 'banana'}
# TypeError, unsupported operand type(s) for +: 'dict' and 'dict'

```



## 참고 자료

[python tutor](https://pythontutor.com/visualize.html#mode=edit)

