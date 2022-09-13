from math import factorial


n, k = map(int,input().split())

# 1 <= n <= 10, 0 <= k <= n
#? 조합 공식 : n! / k!(n-k!)

b = factorial(n) // (factorial(k) * factorial(n - k))
print(b)

# N, K = map(int, input().split())

# result = 1
# for i in range(K):
#     result *= N
#     N -= 1

# divisor = 1
# for i in range(2, K+1):
#     divisor *= i

# print(result // divisor)

# n,k=map(int, input().split())
# a = 1
# b = 1
# while k:
#     a*=n
#     b*=k
#     n-=1
#     k-=1
# print(a//b)

# L = list(map(int,input().split()))
# n =L[0]
# k =L[1]
# m = 1

# for i in range(k):
#     m = m*(n-i)/(i+1)

# print(int(m))