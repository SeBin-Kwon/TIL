n = int(input())

while True:
    f = True
    for i in str(n):
        if i != '4' and i != '7':
            f = False
            n -= 1
    if f:
        print(n)
        break