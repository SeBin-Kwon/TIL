a, b = map(int,input().split())
print(bool(a and b) or bool((not b) and (not a)))