T = int(input())
for t in range(1,T+1):
    n = int(input()) # 카드 개수
    card = input().split() # 카드들
    shuf = [] # 셔플 했을 때의 카드들
    
    # 슬라이싱으로 절반을 각각 new1, new2에 넣기
    if n % 2 == 0:
        new1 = card[:n//2]
        new2 = card[n//2:]
    else: # 홀수라면 +1해서 넣기
        new1 = card[:n//2+1]
        new2 = card[n//2+1:]
    
    # new1이나 new2에 카드가 있다면 계속 반복하기
    while new1 or new2:
        # 만약 new1가 비어있지 않다면 (True라면)
        if new1:
            # new1의 첫번째를 꺼내서 셔플에 넣기
            shuf.append(new1.pop(0))
            
        # new2도 똑같이 해줌
        if new2:
            shuf.append(new2.pop(0))

    print(f'#{t}', *shuf)