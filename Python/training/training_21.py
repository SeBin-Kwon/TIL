n = int(input())
while n > 0 :
    a = n % 10
    n //= 10
    print(a, end='')