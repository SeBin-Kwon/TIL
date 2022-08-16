t = int(input())
for _ in range(t):
    a = input().split()
    r = ''
    for i in range(len(a)):
        r += a[i][::-1]+' '
    print(r)
