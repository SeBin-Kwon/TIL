T = 10
for t in range(1,T+1):
    n = int(input())
    box = list(map(int,input().split()))

    for j in range(n):
        idx = box.index(max(box))
        box[idx] = max(box) - 1
        idx = box.index(min(box))
        box[idx] = min(box) + 1

    print(f'#{t}', max(box)-min(box))