import sys
sys.stdin = open('2056.txt', 'r')

T = int(input())
dic = {
    '01' : 31,
    '02' : 28,
    '03' : 31,
    '04' : 30,
    '05' : 31,
    '06' : 30,
    '07' : 31,
    '08' : 31,
    '09' : 30,
    '10' : 31,
    '11' : 30,
    '12' : 31
}

for t in range(1,T+1):
    c = input()
    y = c[:4]
    m = c[4:6]
    d = c[6:]

    if m not in dic:
        print(f'#{t} -1')
        continue

    if 0 < int(d) <= dic[m]:
        print(f'#{t} {y}/{m}/{d}')
    else:
        print(f'#{t} -1')