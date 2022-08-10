dic = {}
n = int(input())
cnt = 0

for _ in range(n):
    cow, p = map(int,input().split())

    if cow not in dic:
        dic[cow] = p
    else:
        if dic[cow] != p:
            cnt += 1
            dic[cow] = p
    
print(cnt)