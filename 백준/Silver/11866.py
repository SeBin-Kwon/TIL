from collections import deque
import sys
sys.stdin = open('11866.txt','r')

n, k = map(int,input().split())
l = deque([i for i in range(1,n+1)])
y = []

while l:
    for i in range(k-1):
        l.append(l.popleft())
    y.append(l.popleft())

print('<',end='')
for j in y:
    if j == y[-1]:
        print(j,end='')
    else:
        print(f'{j}, ',end='')
print('>',end='')
