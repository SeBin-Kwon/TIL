import sys
sys.stdin = open('1057.txt', 'r')
input = sys.stdin.readline

n, j, h = map(int,input().split())
cnt = 0
while j != h:
    if j % 2 != 0:
        j += 1
    if h % 2 != 0:
        h += 1
    j //= 2
    h //= 2
    cnt += 1
print(cnt)