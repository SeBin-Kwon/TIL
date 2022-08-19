T = int(input())
cnt = 0

for _ in range(T):
    tc = int(input())
    student = list(map(int,input().split()))
    for i in student: # 점수 받기
        if cnt < student.count(i): # 카운트한 수가 더 크다면
            cnt = student.count(i) # 변수에 할당
            m = i # 해당 수 할당
        elif cnt == student.count(i): # 만약 카운트한 수가 같다면
            m = max(m, i) # 둘중에 더 큰 수 할당
    print(f'#{tc} {m}')
    cnt = 0 # 카운트 초기화