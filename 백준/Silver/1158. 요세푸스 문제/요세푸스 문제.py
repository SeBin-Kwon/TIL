import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
l = deque([i for i in range(1,n+1)])
result = []

while l:
    for i in range(k-1):
        l.append(l.popleft())
    result.append(l.popleft())
    
print('<',end='')
print(*result, sep=', ',end='')
print('>',end='')