n, m = map(int,input().split())
num = list(map(int,input().split()))
result = []

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            sum_ = num[i] + num[j] + num[k]
            if sum_ <= m:
                result.append(sum_)               
            else:
                continue
                
print(max(result))