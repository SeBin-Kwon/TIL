r,c = map(int,input().split())
p = [list(input()) for _ in range(r)]

car = [0]*5

for i in range(r-1):
    for j in range(c-1):
        t = []
        t.append(p[i][j])
        t.append(p[i][j+1])
        t.append(p[i+1][j+1])
        t.append(p[i+1][j])

        if '#' not in t:
            if t.count('.') == 4:
                car[0] += 1
            elif t.count('.') == 3 and t.count('X') == 1:
                car[1] += 1
            elif t.count('.') == 2 and t.count('X') == 2 :
                car[2] += 1
            elif t.count('.') == 1 and t.count('X') == 3 :
                car[3] += 1
            elif t.count('.') == 0 and t.count('X') == 4 :
                car[4] += 1
for i in car:
    print(i)