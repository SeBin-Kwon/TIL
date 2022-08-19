T = int(input())
m = 'aeiou'
for t in range(1,T+1):
    # 결과값 넣을 변수
    result = ''
    s = input()
    # 문자 확인
    for i in s:
        # 해당 문자가 모음에 속하지 않으면
        if i not in m:
            # 결과값에 추가
            result += i
    print(f'#{t} {result}')