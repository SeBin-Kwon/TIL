n = int(input())
s = list(map(int,input().split()))
l = []
cnt = 0

for i in range(n):
    if s[i] not in l:
        l.append(s[i])
    else:
        cnt += 1
print(cnt)