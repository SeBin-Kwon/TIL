T = int(input())
for t in range(T):
    h, w, n = map(int,input().split())
    cnt = 0

    hotel = [[0] * w for _ in range(h)]

    for i in range(w):
        for j in range(h):
            hotel[j][i] = 1
            cnt += 1

            if cnt == n:
                nh = str(j+1)
                nw = str(i+1)
                break
    

    print(nh+nw.zfill(2))