n = int(input())
s = 1
for i in range(n):
    if s == 1:
        print(1, end=' ')
    s *= 2
    print(s, end=' ')