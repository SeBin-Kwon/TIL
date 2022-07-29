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
```

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

## 1764번 듣보잡

```python
```

