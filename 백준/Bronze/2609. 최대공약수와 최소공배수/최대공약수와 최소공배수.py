a, b = map(int,input().split())

max_ = 0
for i in range(1, min(a,b)+1):
    if a % i == 0 and b % i == 0:
        max_ = i
min_ = a*b//max_ 
print(max_)
print(min_)