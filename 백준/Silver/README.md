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

