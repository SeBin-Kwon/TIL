import sys
input = sys.stdin.readline

n, k = map(int,input().split())

coins = []
for i in range(n):
    coin = int(input())
    if coin <= k:
        coins.append(coin)
cnt = 0
for i in coins[::-1]:
    cnt += k // i
    k = k % i
    if k == 0:
        break
print(cnt)