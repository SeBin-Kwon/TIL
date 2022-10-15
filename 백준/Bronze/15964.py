def f(a,b):
    result = (a+b)*(a-b)
    return result
a, b = map(int,input().split())
print(f(a,b))