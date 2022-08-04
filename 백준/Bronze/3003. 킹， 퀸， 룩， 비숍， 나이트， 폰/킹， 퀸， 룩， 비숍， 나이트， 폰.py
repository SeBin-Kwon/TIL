pies = [1, 1, 2, 2, 2, 8]
white = list(map(int,input().split()))
result = []

for i in range(len(pies)):
    result.append(pies[i] - white[i])
print(*result)