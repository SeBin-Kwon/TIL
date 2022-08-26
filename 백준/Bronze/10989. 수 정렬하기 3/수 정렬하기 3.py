import sys
# sys.stdin = open('10989.txt', 'r')

input = sys.stdin.readline
n = int(input())
m = [0] * 10001

for i in range(n):
    a = int(input())
    m[a] += 1

for j in range(1,10001):
    if m[j] != 0:
        for k in range(m[j]):
            print(j)