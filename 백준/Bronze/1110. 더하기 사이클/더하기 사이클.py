n = input()
# while True: # 종료조건은 n과 결과값이 같을 경우
# 문자열 인덱스 인트 변환 게산
n1 = n # 기존 입력값 유지
a = 0 # 각 자릿수를 int로 변환 후 합친 값
cnt = 0 # 사이클 횟수
new_num = '' # 새로운 수
stop = 0 # 무한 루프 방지용
while True:
    cnt += 1
    if len(n) == 1: # 만약 입력값의 길이가 1이면
        n = '0' + n # 입력값 앞에 '0'을 붙여 두자릿수로 만들기
    for i in n: # 입력값 하나하나 꺼내기
        a += int(i) # 입력값 하나하나 int로 변환 후 합친 값
        s = str(a) # 합친 값을 str으로 변환
    a = 0 # 합친 값 초기화, 다음 사이클에 영향을 주면 안되기 때문

    new_num = n[1]+ s[(len(s)-1)] # 입력값의 두번째와 합친 값의 마지막 숫자 더하기
    n = new_num # 다음 사이클을 위한 할당

    if int(n1) == int(new_num): # 만약 기존 입력값과 새로운 수가 같다면
        break # 멈추기
    if stop > 10:
        break
print(cnt)