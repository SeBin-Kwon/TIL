l = []
for _ in range(5):
    n = int(input())
    l.append(n)
s_l = sorted(l)

print(sum(l)//5, s_l[2], sep='\n')