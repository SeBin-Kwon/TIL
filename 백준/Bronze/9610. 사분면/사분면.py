n = int(input())
dic = {
    'Q1' : 0,
    'Q2' : 0,
    'Q3' : 0,
    'Q4' : 0,
    'AXIS' : 0
}

for _ in range(n):
    x, y = map(int,input().split())
    if x > 0 and y > 0:
        dic['Q1'] += 1
    elif x < 0 and y > 0:
        dic['Q2'] += 1
    elif x < 0 and y < 0:
        dic['Q3'] += 1
    elif x == 0 or y == 0:
        dic['AXIS'] += 1
    else:
        dic['Q4'] += 1
for k,v in dic.items():
    print(f'{k}: {v}')