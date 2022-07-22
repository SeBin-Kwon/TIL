l = []
for i in range(9):
    n = int(input())
    l.append(n)
print(max(l), l.index(max(l))+1, sep='\n')