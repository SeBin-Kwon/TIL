t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    cnt = 0
    if n == 0:
        cnt += 1

    for i in range(n,m+1):
        while i // 10 > 0:
            r = i % 10
            if r == 0 and i // 10 != 0:
                cnt += 1
            i = i // 10
    print(cnt)