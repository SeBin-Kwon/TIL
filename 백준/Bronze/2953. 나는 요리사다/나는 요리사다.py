l = []
for i in range(5):
    a = sum(map(int,input().split()))
    l.append(a)
print(l.index(max(l))+1,max(l))