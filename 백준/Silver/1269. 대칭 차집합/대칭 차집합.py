a, b = map(int,input().split())
a_set = set(map(int,input().split()))
b_set = set(map(int,input().split()))

for i in list(a_set):
    if i in b_set:
        a_set.remove(i)
        b_set.remove(i)
print(len(a_set)+len(b_set))