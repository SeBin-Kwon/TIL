# SWEA_D2_1284

```python
# A사 : W * P원
# B사 :
# 	R 이하 : Q
# 	R 초과 : Q + S*(W-R)

T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A = W * P
    # B = Q if W <= R else Q + S *(W-R)
    if R > W:
        B = Q
    else:
        B = Q + S*(W-R)
    print(f'#{test_case}{min(A,B)}')
```

> - 주석처리 하면서 풀거나
> - 공책에 적으면서 풀기



# SWEA D2 1288

```python
t = int(input())
for test_case in range(1,t+1):
    # Input 가져오기 (첫번째 값 -> 1)
    n = int(input())
    n1 = n # n이 증폭되지 않도록 복제해놓기
    # 기록지
    numbers = set()
    # while 반복 => set 길이가 10이 될때까지
    while len(numbers) < 10:
        # for 반복 : 숫자를 문자로
        for n in str(n):
        # numbers set에 추가
            numbers.add(n)
        if len(numbers) == 10:
            break # while문 멈추기
        n += n1 # 등차수열 이용, n*cnt OK, while문 멈추면서 더하지 않는다.
    print(f'#{test_case} {n}')
```

