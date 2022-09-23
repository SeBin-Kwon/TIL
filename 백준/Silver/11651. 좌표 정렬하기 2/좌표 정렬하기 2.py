import sys
input = sys.stdin.readline

n = int(input())
xy = []
for i in range(n):
    x, y = map(int,input().split())
    xy.append((x,y))
result = sorted(xy, key=lambda x: (x[1],x[0]))
for i in result:
    print(*i)