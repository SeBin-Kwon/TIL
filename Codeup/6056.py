a, b = map(int,input().split())
print(bool(a and (not b)) or bool(b and (not a)))