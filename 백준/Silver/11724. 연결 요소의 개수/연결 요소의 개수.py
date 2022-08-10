import sys
input = sys.stdin.readline
n, m = map(int,input().split()) # 정점 개수, 간선 개수

 # 인접리스트 생성
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

v = [False] * (n + 1)
cnt = 0

def dfs(start):
    stack = [start]
    v[start] = True
    while stack:
        cur = stack.pop()
        for j in graph[cur]:
            if not v[j]:
                v[j] = True
                stack.append(j)
        
for k in range(1,n+1):
    if v[k] == False:
        dfs(k)
        cnt += 1

        
print(cnt)