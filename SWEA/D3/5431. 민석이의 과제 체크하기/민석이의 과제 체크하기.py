T = int(input())
for t in range(1, T+1):
    n, k = map(int,input().split())
    none = []
    k_list = list(map(int,input().split()))
    for p in range(1,n+1):
        if p not in k_list:
            none.append(p)

    print(f'#{t}',*none)