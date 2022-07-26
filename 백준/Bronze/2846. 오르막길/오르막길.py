n = int(input())
p = list(map(int,input().split()))
l = []
h = 0

for i in range(n-1):
    if p[i] < p[i+1]:
        h += p[i + 1] - p[i]
    if p[i] >= p[i+1]:
        l.append(h)
        h = 0
l.append(h)

print(max(l))