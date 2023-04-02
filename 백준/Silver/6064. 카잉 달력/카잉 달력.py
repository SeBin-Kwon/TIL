for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    ans = -1
    while x <= m*n:
        if (x-y) % n == 0:
            ans = x
            break
        x += m
    print(ans)