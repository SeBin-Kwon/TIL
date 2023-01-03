import sys

input = sys.stdin.readline

dp = [0] * 41
dp[0] = (1, 0)
dp[1] = (0, 1)
dp[2] = (1, 1)

for i in range(3, 41):
    dp[i] = (dp[i-1][1], sum(dp[i-1]))

T = int(input())
for t in range(T):
    n = int(input())
    print(*dp[n])