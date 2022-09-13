T = int(input())
for t in range(T):
    h, w, n = map(int,input().split())
    nh = n % h
    nw = n // h + 1
    if nh == 0:
        nh = h
        nw = n // h
    print(nh*100+nw)