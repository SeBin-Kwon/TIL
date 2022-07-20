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

