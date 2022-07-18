# 실습 문제 풀이 3

## 문제 15 문자의 위치 구하기

```python
# 15. 문자의 위치 구하기 (처음으로)
# 없으면 -1
word = 'banana'

# 1. for - else

# 문자로 순회하는 것이 아니라! 
# 인덱스로 접근해서 쓰자.
# 원하는 숫자? 0, 1, 2, 3, 4, 5
# 얻는 방법은? range(len(word)) => range(6) => 0 ~ 5
for idx in range(len(word)):
    # print(idx, word[idx])
    # 알파벳이 a일때 
    if word[idx] == 'a':
        print(idx)
        break
# for문을 다 돌았다는 뜻은
# 한번도 break에 안걸렸다.
# 즉, a는 없었다.
else:
    print(-1)

# 2. for - else
# a가 있었냐? 없었냐? (boolean)
is_a = False
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx)
        is_a = True
        break

if not is_a:
    print(-1)
    
# 15-1

# 1. 리스트에 담는다!
word = 'banana'
result = []
for idx in range(len(word)):
    if word[idx] == 'a':
        # 리스트에 추가해줘
        result.append(idx)
print(result)

# 2. 그때 그때 출력
word = 'banana'
result = []
for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx, end=' ')
```

- 'banana'의 a에 처음으로 도달했을 때,

  [0] 'b' False / [1] 'a' True

  - 문자로 순회하는 것이 아니라 **인덱스**로 접근 => `range`
  - for - else 문

- boolean을 활용해서 for-else 대체 가능

  - 얘가 들어왔는지 안들어왔는지 알고싶어 => `boolean`



## 문제 16 모음 등장 여부 확인하기

```python
# 모음의 갯수
# a, e, i, o, u
word = 'apple'

# 지금은 인덱스가 필요없어서
# 그냥 char를 받을게요!

# 1.
count = 0
for char in word:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1
print(count)

# 2. 
count = 0
for char in word:
    # ['a', 'e', 'i', 'o', 'u']
    if char in 'aeiou':
        count += 1
print(count)

# in 
word = 'apple'
is_a = False
for char in word:
    if char == 'a':
        is_a = True

print(is_a)
print('a' in word)
```

`if char in 'aeiou' :` 만약 word에 있는 문자열이 'aeiou' 중에 포함이 된다면



## 문제 18 알파벳 등장 개수 구하기

```python
word = 'banana'

# 1. 풀이
result = {}
for char in word:
    # 딕셔너리에 키가 없으면?
    if not char in result:
        # 키랑 값을 1으로 초기화한다.
        result[char] = 1
    # 딕셔너리에 키가 있으면?
    else:
        result[char] = result[char] + 1
print(result)


result = {}
for char in word:
    # result['a'] 없으면 KeyError
    # result.get('a') 기본값이 None
    # result.get('a', 0) 기본값이 0
    result[char] = result.get(char, 0) + 1
print(result)

# 출력부분
for key in result:
    print(key, result[key])
```

### 왜 딕셔너리인가?

> b 1
>
> a 1 어? a 있네? 2
>
> n 1

- 있으면? +1 없으면? 0

#### 딕셔너리에 키가 없으면?

- `if not char in result:` 

  캐릭터가 딕셔너리안에 없으면 

- `result[char] = 1`

  키랑 값을 1로 초기화한다.

#### 딕셔너리에 키가 있으면?

- `else: result[char] += 1`

  기존것에 더해준다

  

## 딕셔너리 해설

```python
word = 'banana'
result = {}
# 키-값의 쌍 추가
result['a'] = 0
print(result) # { a : 0 }

# 값의 추가
my_list = []
my_list.append(1)
print(my_list)

# 문자열을 반복하면서 알파벳 하나씩이 char
for char not in word:
  # 만약에 기존에 키가 없으면, 1로 초기화를 하고
  # result[char] # 없으면 KeyError
  # result.get(char, 0) # 없으 None 반환, 디폴트값 있으면 0
  if char in result:
    result[char] = 1
  else:
    result[char] = result[char] + 1
  # 키가 있으면, 기존 값에 더하자
```

### 데이터를 기록할 때

> a 3, b 3 

- key, value => 딕셔너리

> strawberry, blueberry

- 값들의 나열 => 리스트
- 중복 제거 => 세트