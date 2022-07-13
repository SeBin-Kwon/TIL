#4번 문제 n까지의 곱
n = 5
result = 1
a = 1

while a <= n :
    result *= a
    a += 1
print(result)

for i in range(1,n+1):
    result *= i
print(result)
