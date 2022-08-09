r,c = map(int,input().split())
p = [list(input()) for _ in range(r)]

car = [0]*5

for i in range(r-1):
    for j in range(c-1):
        l = p[i][j] + p[i][j+1] + p[i+1][j] + p[i+1][j+1]
        if '#' not in l:
            car[l.count('X')] += 1
for i in car:
    print(i)