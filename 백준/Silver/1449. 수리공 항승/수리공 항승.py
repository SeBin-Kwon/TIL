import sys
input = sys.stdin.readline

n,l = map(int,input().split())
pipe = list(map(int,input().split()))
pipe.sort()

cnt = 1

end = pipe[0]+l

for i in range(n):
    if pipe[i] < end:
        continue
    else:
        end = pipe[i]+l
        cnt += 1
print(cnt)