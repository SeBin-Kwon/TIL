T = int(input())
for t in range(1,T+1):
    n, d = map(int,input().split())
    x = d * 2 + 1
    r = n // x
    if n % x:
        r += 1
    print(f'#{t}', r)