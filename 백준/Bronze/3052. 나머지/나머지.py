number = []
for _ in range(10):
    n = int(input())
    number.append(n)

result = []
for i in number:
    result.append(i % 42)
result = list(set(result))
print(len(result))