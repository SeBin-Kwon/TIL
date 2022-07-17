n = int(input())
a = input().split()
b = []
a = a[::-1]
for i in range(n):
    a[i] = int(a[i])
for i in range(n):
    print(a[i], end=' ')
