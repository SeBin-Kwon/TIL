import sys
sys.stdin = open('25192.txt', 'r')

import sys
input = sys.stdin.readline

N = int(input())
name = []
cnt = 0

for _ in range(N):
    n = input()
    
    if n == 'ENTER':
        cnt += len(name)
        name = []

    elif n not in name:
        name.append(n)

print(cnt+len(name))

