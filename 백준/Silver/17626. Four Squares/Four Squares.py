import sys
input = sys.stdin.readline
n = int(input())
dp = [0, 1]
for i in range(2, n+1):
    min_ = 4
    j = 1
    while (j**2) <= i:
        min_ = min(min_, dp[i-j**2])
        j += 1
    dp.append(min_ + 1)
print(dp[n])