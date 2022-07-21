# t = int(input())
# for test_case in range(1,t+1):
#     n = int(input())
    # while 사용
    # 0~9까지 확인하기
    # 리스트의 인덱스 활용해서 숫자 n이면 n번째에 체크
    # list = [0]*10
    # cnt = 0
    # while True:
    #     result = str(n*cnt)
    #     for i in range(len(result)):
    #         list[int(result[i])] = 1
    #     if 0 not in list:
    #         break   
    #     else:
    #         cnt += 1
    # print(f'#{test_case} {result}') 

t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    # set으로 풀기
    # l = []
    s = set()
    cnt = 0
    while len(s) < 10: # 0~9 다 수집하기 전까지 반복 # todo 같으면 계속 반복, 작게 설정하고 if 같으면 break 걸기
        cnt += 1
        result = str(n*cnt)
        for i in result:
            s.add(i)
        if len(s) == 10:
            break
    print(f'#{test_case} {result}')
