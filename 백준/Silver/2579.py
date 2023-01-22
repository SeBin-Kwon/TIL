import sys
sys.stdin = open('2579.txt', 'r')
input = sys.stdin.readline

n = int(input())
stairs = [0] * 301
dp = [0] * 301
for i in range(n):
    stairs[i] = int(input())

dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])
print(dp[n - 1])

