t = int(input())
s = 0
for test_case in range(1,t+1):
    n = int(input())
    for i in range(1,n+1):
        if i%2 != 0:
            s += i
        else:
            s -= i
    print(f'#{test_case}', s)
    s = 0