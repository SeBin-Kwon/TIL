import sys
sys.stdin = open('1213.txt', 'r')

for t in range(1,11):
    n = int(input())
    r = input()
    s = input()
    print(f'#{t} {s.count(r)}')
