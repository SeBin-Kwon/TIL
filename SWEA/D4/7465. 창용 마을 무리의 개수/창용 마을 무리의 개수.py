T = int(input())
for t in range(1,T+1):
    n, m = map(int,input().split())
    p = [[] for _ in range(n+1)]
    cnt = 0

    for i in range(m):
        a, b = map(int,input().split())
        p[a].append(b)
        p[b].append(a)
    
    v = [False] * (n+1)
    
    def dfs(start):
        stack = [start]
        v[start] = True

        while stack:
            node = stack.pop()
            for adj in p[node]:
                if not v[adj]:
                    v[adj] = True
                    stack.append(adj)


    for j in range(1, n+1):
        if v[j] == False:
            dfs(j)
            cnt += 1

    print(f'#{t}', cnt)