import sys
sys.stdin = open('1003.txt', 'r')
input = sys.stdin.readline

# zero = [1, 0, 1]
# one = [0, 1, 1]

# def fibonacci(n):
#     length = len(zero)
#     if n >= length:
#         for i in range(length, n+1):
#             zero.append(zero[i-1] + zero[i-2])
#             one.append(one[i-1] + one[i-2])
#     print(zero[n], one[n])
# T = int(input())
# for t in range(T):
#     n = int(input())
#     fibonacci(n)

# dp = [0] * 41
# dp[0] = (1, 0)
# dp[1] = (0, 1)
# dp[2] = (1, 1)

# for i in range(3, 41):
#     dp[i] = (dp[i-1][1], sum(dp[i-1]))

# T = int(input())
# for t in range(T):
#     n = int(input())
#     print(*dp[n])

T = int(input())
for t in range(T):
    n = int(input())
    zero, one = 1, 0
    for i in range(n):
        zero, one = one, zero + one
    print(zero, one)