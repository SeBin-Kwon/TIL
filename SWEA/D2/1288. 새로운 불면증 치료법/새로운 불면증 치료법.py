t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    l = [0]*10
    k = 0
    while True:
        if 0 not in l:
            break
        else:
            k += 1
            num = str(n*k)
            for i in range(len(num)):
                l[int(num[i])] = 1
    print(f'#{test_case} {num}')