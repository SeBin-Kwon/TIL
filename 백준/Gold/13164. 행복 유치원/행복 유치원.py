import sys
input = sys.stdin.readline

n, k = map(int,input().split())
l = list(map(int,input().split()))
costs = []

for i in range(n-1):
    costs.append(l[i+1] - l[i])
costs.sort()

print(sum(costs[:n-k]))