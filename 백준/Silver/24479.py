import sys
sys.stdin = open('24479.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort()

visited = [0] * (n+1)
cnt = 1

def dfs(r):
    global cnt
    visited[r] = cnt
    for i in graph[r]:
        if not visited[i]:
            cnt += 1
            dfs(i)
dfs(r)
for i in range(1,n+1):
    print(visited[i])


# def dfs(r):
#     print(r)
#     visited[r] = 1
#     for i in graph[r]:
#         if not visited[i]:
#             visited[i] = 1
#             dfs(i)
# dfs(r)
# for i in range(1,n+1):
#     if visited[i] == 0:
#         print(0)

# def dfs(r):
#     stack = [r]
#     result = [0] * (n+1)
#     cnt = 1
#     while stack:
#         r = stack.pop()
#         result[r] = cnt
#         cnt += 1
#         visited[r] = 1
#         for i in graph[r]:
#             if not visited[i]:
#                 visited[i] = 1
#                 stack.append(i)
                
#     return result

# result = dfs(r)
# for i in range(1,n+1):
#     print(result[i])