n, k = map(int,input().split())
x = sorted(list(map(int,input().split())),reverse=True)
result = x[:k]
print(min(result))
