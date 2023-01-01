n = int(input())
p = list(map(int,input().split()))
p.sort()
sum_ = 0
result = 0
for i in p:
    sum_ += i
    result += sum_
print(result)