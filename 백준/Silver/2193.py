import sys
sys.stdin = open('2193.txt', 'r')
input = sys.stdin.readline

# n자리수
# 1 : 1 - 1
# 2 : 10 - 1
# 3 : 100 101 - 2
# 4 : 1000 1010 1001 - 3
# 5 : 10000 10001 10101 10010 10100 - 5

# dp[n] = dp[n-2]+dp[n-1]

n = int(input())

def pinary_dp(n):
    pinary = [0, 1, 1]
    for i in range(3, n+1):
        pinary.append(pinary[i-2] + pinary[i-1])
    return pinary[-1]

print(pinary_dp(n))