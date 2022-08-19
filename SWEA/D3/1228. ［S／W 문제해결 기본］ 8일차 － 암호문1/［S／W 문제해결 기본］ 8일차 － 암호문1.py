for tc in range(1,11):
    # 원본 암호문의 길이
    n = int(input())
    # 원본 암호문
    origin = input().split()
    # 명령어의 개수
    m = int(input())
    # 명령어
    command = input().split()

    for i in range(len(command)):       
        if command[i] == 'I': # 명령어가 시작되는 'I'라면
            position = int(command[i+1]) # 두번째 위치 값 정수로 저장
            cnt = int(command[i+2]) # 세번째 개수 값 정수로 저장

            # 원본에 삽입하기
            for j in range(cnt): # 명령어 개수만큼 반복
                origin.insert(position+j ,command[i+3+j])
                # 넣어야 할 위치부터 시작해서 차례로 넣기
                # 명령어가 i에서 네번째 부터 시작하므로 i+3에서 차례로 값 넣기


    print(f'#{tc}', end=' ')
    print(*origin[:10])