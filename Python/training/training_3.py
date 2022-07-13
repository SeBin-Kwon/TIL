# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
n = 10
result = 0
a = 0
while a <= n :
    result += a
    a += 1
print(result)

n = 10
result = 0
a = 0
for a in range(n):
    a += 1
    result += a
print(result)

# n=int(input())
# r=0

# for i in range(n+1):
#     r+=i

# while n!=0:
#     r+=n
#     n-=1

# print(r)