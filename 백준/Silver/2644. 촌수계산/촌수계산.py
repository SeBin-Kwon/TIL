n = int(input())
a, b = map(int,input().split())
m = int(input())

f = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    f[x].append(y)
    f[y].append(x)

visited = [False] * (n+1)
answer = -1

stack = [(a, 0)]
visited[a] = True
while stack:
    num, cnt = stack.pop()
    
    for adj in f[num]:
        if not visited[adj]:
            visited[adj] = True
            stack.append((adj, cnt+1))

    if num == b:
        answer = cnt
        break
        
print(answer)