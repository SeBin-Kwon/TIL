a, b = map(int,input().split())
a_elem = list(map(int,input().split()))
b_elem = list(map(int,input().split()))

a_set = set(a_elem)
b_set = set(b_elem)

for i in list(a_set):
    if i in b_set:
        a_set.remove(i)
        b_set.remove(i)
print(len(a_set)+len(b_set))