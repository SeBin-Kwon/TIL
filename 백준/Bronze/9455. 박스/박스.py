import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n, m = map(int,input().split())
    box = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0

    for i in range(m):
        for j in range(n-1):
            for k in range(j+1,n):
                if box[j][i] > box[k][i]:
                    cnt += 1
    print(cnt)