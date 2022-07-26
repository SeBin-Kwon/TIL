n = int(input())
result = 0
for i in range(1, n+1):
    a = sum(list(map(int, str(i))))
    if i + a == n:
        result = i
        break
print(result)