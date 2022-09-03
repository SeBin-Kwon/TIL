dic = {}
cnt = 0

n = int(input())

in_ = [input() for _ in range(n)]
out_ = [input() for _ in range(n)]

for k in range(n):
    dic[in_[k]] = k

for i in range(n-1):
    for j in range(i+1,n):
        if dic[out_[i]] > dic[out_[j]]:
            cnt += 1
            break
print(cnt)