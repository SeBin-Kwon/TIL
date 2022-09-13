from math import factorial


n, k = map(int,input().split())

# 1 <= n <= 10, 0 <= k <= n
#? 조합 공식 : n! / k!(n-k!)

b = factorial(n) // (factorial(k) * factorial(n - k))
print(b)