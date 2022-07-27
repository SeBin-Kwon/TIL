sum_ = 0
for i in range(10):
    n = int(input())
    sum_ += n
    if sum_ >= 100:        
        if sum_ - 100 > 100 - (sum_ - n):
            sum_ -= n
        break
print(sum_)