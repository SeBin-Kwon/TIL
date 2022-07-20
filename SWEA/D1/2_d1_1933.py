n = int(input())
for i in range(n,0,-1):
    if n%i == 0:
        print(n//i, end=' ')