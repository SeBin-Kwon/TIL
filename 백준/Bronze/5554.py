sum_ = 0
for i in range(4):
    sum_ += int(input()) 

m = sum_ // 60
s = sum_ % 60

print(m, s, sep='\n')