T = int(input())
for t in range(1,T+1):
    n = int(input())
    num = list(map(int,input().split()))
    result = []
    for i in range(n):
        a = num[i] // 10
        b = num[i] % 10
        result.append(a**b)
    print(f'#{t}', sum(result))