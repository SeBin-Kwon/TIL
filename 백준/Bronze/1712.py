import sys
sys.stdin = open('1712.txt', 'r')
a,b,c = map(int,input().split())
if c <= b:
    print(-1)
else:
    print((a // (c - b)) + 1)