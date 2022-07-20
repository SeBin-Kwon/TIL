t = int(input())
for test_case in range(1,t+1):
    p,q,r,s,w = map(int,input().split())
    a = w * p
    b = q if w < r else q+(w-r)*s
    print(f'#{test_case} {min(a,b)}')