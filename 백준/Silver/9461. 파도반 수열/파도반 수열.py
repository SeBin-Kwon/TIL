import sys
input = sys.stdin.readline

p = [1,1,1]
for i in range(97):
    p.append(p[-3] + p[-2])
for i in range(int(input())):
    n = int(input())
    print(p[n-1])
