n = list(map(int,input().split()))
sum_ = 0
for i in n:
    sum_ += i**2
    result = sum_ % 10
print(result)