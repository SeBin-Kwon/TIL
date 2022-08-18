n_a, n_b = map(int,input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))

print(len(a-b))
print(*sorted(a-b))