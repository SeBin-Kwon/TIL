n, m = map(int,input().split())
n -= 1
m -= 1
w = abs(n//4 - m//4)
h = abs(n%4 - m%4)
print(w+h)