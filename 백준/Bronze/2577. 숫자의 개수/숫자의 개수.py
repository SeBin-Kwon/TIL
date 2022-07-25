a = int(input())
b = int(input())
c = int(input())
l = [0]*10
d = a*b*c
for i in str(d):
    l[int(i)] += 1
for j in l:
    print(j)