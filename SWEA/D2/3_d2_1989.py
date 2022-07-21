# 문자열을 인덱스로 접근해서 거꾸로 돌렷을때
# 원래 문자열과 똑같다면 1, 아니면 0
t = int(input())
for test_case in range(1,t+1):
    a = input()
    if a == a[::-1]:
        print(f'#{test_case} {1}')
    else:
        print(f'#{test_case} {0}')

    