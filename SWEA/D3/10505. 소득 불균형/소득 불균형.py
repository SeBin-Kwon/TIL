T = int(input())
l = [] # 평균 이하 사람 담을 리스트

for tc in range(1, T+1):
    n = int(input())    # 소득 개수
    money = list(map(int,input().split()))
    avg = sum(money)//n # 평균 구하기
    for i in range(len(money)):
        if money[i] <= avg: # 만약 평균 이하라면
            l.append(i) # 리스트에 담기
 
    print(f'#{tc} {len(l)}')
    l = [] # 리스트 초기화