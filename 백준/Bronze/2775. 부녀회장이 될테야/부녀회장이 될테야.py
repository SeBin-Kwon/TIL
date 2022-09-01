T = int(input())
for t in range(T):
    k = int(input())
    n = int(input())
    s = [i for i in range(1,n+1)]
    for j in range(k):
        for k in range(1,n):
            s[k] += s[k-1]
    print(s[-1])