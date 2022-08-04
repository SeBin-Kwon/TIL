a, b = input().split()

min_ = int(a.replace('6','5')) + int(b.replace('6','5'))
max_ = int(a.replace('5','6')) + int(b.replace('5','6'))

print(min_, max_)
        
