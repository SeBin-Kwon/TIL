T = int(input())
for t in range(1, T+1):
    n, q = map(int,input().split())
    box = [0] * n
    for i in range(1,q+1):
        l, r = map(int,input().split())
        for j in range(l-1,r):
            box[j] = i
    print(f'#{t} {" ".join(map(str, box))}')