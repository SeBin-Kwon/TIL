t = int(input())
for test_case in range(1,t+1):
    q = list(input())
    cnt = 0
    score = 0
    for i in q:
        if i == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0
    print(score)