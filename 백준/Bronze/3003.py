
piece = [1, 1, 2, 2, 2, 8]
white = list(map(int,input().split()))
result = []

for i in range(len(piece)):
    result.append(piece[i] - white[i])
print(*result)

# a = [1, 1, 2, 2, 2, 8]
# b = list(map(int, input().split()))
# for i in range(6):
#     print(a[i] - b[i])