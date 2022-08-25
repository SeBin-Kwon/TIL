import sys
sys.stdin = open('1859.txt', 'r')

T = int(input())
for t in range(1,T+1):
    n = int(input())
    period = list(map(int,input().split()))
    buy = 0
    sell = 0
    result = 0
    for i in range(n-1):
        if period[i] <= period[i + 1]:
            buy += period[i]
        elif buy != 0 and period[i] > period[i + 1]:
            sell += period[i]

    print(f'#{t} {buy} {sell}')
