import sys
sys.stdin = open('13164.txt', 'r')
input = sys.stdin.readline

n, k = map(int,input().split())
l = list(map(int,input().split()))
costs = []

for i in range(n-1):
    costs.append(l[i+1] - l[i])
costs.sort()

print(sum(costs[:n-k]))

# visited = [0] * n
# cost = 0
# cnt = 0
# while cnt < k:
#     for i in range(n-1):
#         if not visited[i] and not visited[i+1]:
#             gap = l[i+1] - l[i]
#             if cost == gap:
#                 cnt += 1
#                 visited[i+1] = 1
#                 visited[i] = 1
#         else:
#             if not visited[i]:
#                 visited[i] = 1
#                 cnt += 1
#             elif not visited[i+1]:
#                 visited[i+1] = 1
#                 cnt += 1
#     cost += 1
# print(cnt)