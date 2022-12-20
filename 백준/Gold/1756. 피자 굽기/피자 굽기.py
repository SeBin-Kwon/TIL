import sys
input = sys.stdin.readline

d, n = map(int,input().split())
oven = list(map(int,input().split()))
pizza = list(map(int,input().split()))
cnt = 0

for i in range(1,d):
    if oven[i-1] < oven[i]:
        oven[i] = oven[i-1]

for i in range(d-1,-1,-1):
    if pizza[cnt] > oven[i]:
        continue
    elif pizza[cnt] <= oven[i]:
        cnt += 1
    if cnt == n:
        print(i+1)
        break
    
if cnt != n:
    print(0)