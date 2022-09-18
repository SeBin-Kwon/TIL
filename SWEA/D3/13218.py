import sys
sys.stdin = open('13218.txt', 'r')

T = int(input())
for t in range(1,T+1):
    n = int(input())
    r = n // 3
    print(f'#{t}', r)