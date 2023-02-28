import sys
from itertools import combinations
sys.stdin = open('2961.txt', 'r')
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    s, b = map(int, input().split())
    arr.append((s,b))

result = int(1e9)
for i in range(1,n+1):
    for j in combinations(arr,i):
        s = 1
        b = 0
        for k in j:
            s *= k[0]
            b += k[1]
        result = min(abs(s - b),result)
print(result)