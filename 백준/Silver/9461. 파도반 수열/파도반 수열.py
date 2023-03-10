import sys
input = sys.stdin.readline

def dp(n):
    if n < 3:
        return p[n-1]
    for i in range(3,100):
        p[i] = p[i-3] + p[i-2]
    return p[n-1]

T = int(input())
for t in range(T):
    n = int(input())
    p = [0] * 100
    p[0] = 1
    p[1] = 1
    p[2] = 1
    print(dp(n))
