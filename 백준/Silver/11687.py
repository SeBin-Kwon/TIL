import sys
input = sys.stdin.readline

def find_zeros(n):
    zeros = 0
    while n >= 5:
        zeros += n // 5
        n //= 5
    return zeros

m = int(input())
left, right = 1, m*5

while left <= right:
    mid = (left+right) // 2
    cnt = find_zeros(mid)

    if cnt >= m:
        right = mid - 1
    else:
        left = mid + 1
print(left if find_zeros(left) == m else -1)

# cnt = 0
# n = m
# while m != 0:
#     m //= 5
#     if m != 0:
#         cnt += 1
        
# if n != 1 and n == 5**cnt:
#     print(-1)
# else:
#     print(n * 5 - 5 * cnt)
# d = 1
# for i in range(1,101):
#     d *= i
# print(d)