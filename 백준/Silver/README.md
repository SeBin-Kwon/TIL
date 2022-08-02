# 백준 Python 문제 풀이 Silver

## 7568번 덩치

```python
N= int(input())

S = [list(map(int, input().split())) for i in range(N)]

for x1, y1 in S:
    result = 1
    for x2, y2 in S:
        if x1 < x2 and y1 < y2:
            result += 1


    print(result, end =' ')
```



<br>

## 1065번 한수

```python
n = int(input())
han = 0

for num in range(1,n+1):
    if num <= 99:
        han += 1
    elif num > 99:
        nummber = list(map(int,str(num)))
        if nummber[0] - nummber[1] == nummber[1] - nummber[2]:
            han += 1
print(han)
```

- 첫번째 자리수 - 두번째 자리수 == 두번째 자리수 - 세번째 자리수 = 한수
  - 자리수가 2개인 수는 무조건 한수

<br>

## 7785번 회사에 있는 사람

```python
N = int(input())
logs = dict()
for i in range(N)
    key, valus = input().split()
    logs[key] = value

list_ = []
for key in logs:
    if logs[key] == 'enter':
      list_.append(key)
      
list_.sort(reverse=True)
for name in list_:
    print(name)
```

- 딕셔너리 사용 문제
- value가 출근인 key를 모은다.
- 딕셔너리는 리스트의 상위호환 느낌이므로 꼭 연습해서 마스터하자
- `.sort(reverse=True)`
  - 원본을 덮어 씌우는 것
- `sort()[::-1]`
  - 출력만 거꾸로 출력
  - 원본은 그대로임

<br>

## 1302번 베스트셀러

```python
n = int(input())
dict = {}
result = []

for i in range(n):
    book = input()
    if book not in dict:
        dict[book] = 1
    elif book in dict:
        dict[book] += 1
for k in dict:
    if dict[k] == max(dict.values()):
        result.append(k)
print(sorted(result)[0])
```

1. **key를 기준으로 정렬(오름차순)**

- `sorted(a.key())`

  -  key만 정렬된 값 반환

    `['a', 'c', 'e']`

- `sorted(a.items())`

  - 키를 기준으로 정렬하고 key와 value를 튜플로 묶어서 정렬된 값 반환

    `[('a',2), ('c',4), ('e'.2)]`

2. **value를 기준으로 정렬**

- `sorted(a.value())`

3. **람다식을 이용하여 정렬**

- `sorted(a.items(), key=lambda x: x[0])`
  - x[0]은 key값을 기준으로 정렬하는 것을 의미함

- `sorted(a.items(), key=lambda x: x[1]`
  - x[1]은 value값을 기준으로 정렬하는 것을 의미함

- 내림차순으로 정렬하려면 `sorted(a.key(), **reverse=True**)` 와 같이 마지막에 reverse=True 옵션만 추가해주면 됨

<br>

## 1764번 듣보잡

```python
```

<br>

## 23253번 자료구조는 정말 최고야

```python
# sys.stdin.readline() : 빠르다.
# input() : 느리다.

answer = 'Yes'
stack_list = [[12, 4, 1], [6, 2], [9, 3, 7], [11, 10 ,8, 5]]

for stack in stack_list:
    # stack = [11, 10, 8, 5]
    # stack = [5, 1, 4, 3]
    # 비교값을 pop을 통해서 스택에서 꺼내온다.
    # 5
    comparison = stack.pop()

    # 스택이 비어있지 않을 때 까지
    while len(stack) != 0
        # top comparison 비교
        if stack[-1] > comparison:
            # pop을 사용해서 comparison 값을 갱신
            comparison = stack.pop()
        else:
            answer = 'No'
            break
print(answer)
```

- 맨 위에 있는 값을 pop해서 comparison 변수에 할당, 현재 가장 위에 있는 top과 비교한다.
- 만약 top이 더 크면 pop해서 comparison 변수에 할당
- while문으로 스택이 비어있을 때 까지 비교하고 빼낸다.

<br>

## 9012번 괄호

```python
LEFT = '('
RIGHT = ')'

brackets = ["(", "(", ")", ")", "(", ")", ")"]
left_stack = []
right_stack = []

for bracket in brackets:
    # 괄호가 좌괄호이면
    if bracket == LEFT:
        # left stack push
        left_stack.append(bracket)
    # 괄호가 우괄호이면
    if bracket == RIGHT:
        # 좌괄호 스택의 길이가 0이 아닐 때
        # 좌괄호 스택이 비어있지 않을 때
        if len(left_stack) != 0:
            left_stack.pop()
        # 우괄호를 우괄호 스택에 push
        else:
            right_stack.append(bracket)
if len(left_stack) == 0 and len(right_stack) == 0:
    print('Yes')
else:
    print('No')
```

- 왼쪽 스택에 왼쪽 괄호를 넣고 오른쪽 괄호가 나오면 비어있지 않았을 때 pop해줌
- 오른쪽 괄호가 남고 왼쪽 스택이 비어있을 때, 오른쪽 스택에 넣어줌
- 왼쪽과 오른쪽 스택이 모두 길이가 0일 때 'Yes', 아니면 'No'

<br>
