n = int(input())
m = list(map(int,input().split()))

cnt = 0

for i in m:
    # 1을 제외하고 2부터 자기 자신까지 나누기
    for j in range(2,i+1):
        if i % j == 0:
            if i == j:
                cnt += 1
            # j와 같지 않은데 나누어 떨어지면 합성수이다.
            # 바로 break로 반복문을 빠져나온다.
            break
print(cnt)