n, x = map(int, input().split())
a = map(int, input().split())
for i in a:
    if i < x:
        print(i, end=' ')