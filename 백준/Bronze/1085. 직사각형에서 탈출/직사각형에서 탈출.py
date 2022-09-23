x = list(map(int,input().split()))
a = min(abs(x[0]-x[2]),abs(x[1]-x[3]))
b = min(x[0],x[1])
print(min(a,b))