import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    one = set(map(int,input().split()))
    m = int(input())
    two = list(map(int,input().split()))
    for i in range(m):
        if two[i] in one:
            print(1)
        else:
            print(0)
