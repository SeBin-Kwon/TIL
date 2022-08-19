m = list(map(int,input().split()))
table = [0]*100
total = 0
time = []

for _ in range(3):
    a, b = map(int,input().split())
    time.append(b)
    for i in range(a,b):
        table[i] += 1
        
for i in range(max(time)):
    if table[i] == 1:
        total += m[0]*1
    if table[i] == 2:
        total += m[1]*2
    if table[i] == 3:
        total += m[2]*3
print(total)