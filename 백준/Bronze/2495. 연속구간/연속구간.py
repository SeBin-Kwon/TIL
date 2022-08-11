for _ in range(3):
    n = list(input())
    cnt = 0
    result = [0]

    for i in range(7):
        if n[i] == n[i+1]:
            cnt += 1
            result.append(cnt)
        else:
            cnt = 0
    if result == 0:
        print('1')
    else:
        print(max(result)+1)