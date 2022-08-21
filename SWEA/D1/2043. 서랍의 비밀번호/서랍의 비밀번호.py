p, k = map(int,input().split())
cnt = 0
for i in range(k,p+1):
    cnt += 1
    if i == p+1:
        break
print(cnt)