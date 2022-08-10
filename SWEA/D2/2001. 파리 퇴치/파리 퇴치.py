T = int(input())
for t in range(1, T+1):
    n, m = map(int,input().split())
    fly = [list(map(int,input().split())) for _ in range(n)]
    fly_che = []
    
    for k in range(n-m+1): 
        for l in range(n-m+1): 
            kill = 0
            for i in range(m):
                for j in range(m): 
                    kill += fly[i+k][j+l]
            fly_che.append(kill)

    print(f'#{t}',max(fly_che))