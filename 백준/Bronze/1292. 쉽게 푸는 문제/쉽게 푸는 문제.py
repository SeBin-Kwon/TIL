a, b = map(int,input().split())
num = []
result = 0

for i in range(1,b+1):
    num += [i]*i
for j in range(a-1,b):
    result += num[j]
print(result)
