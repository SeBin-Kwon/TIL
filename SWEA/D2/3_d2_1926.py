
# 정수를 문자열로 바꾸고 인덱스로 접근 후 그 위치의 문자가 3, 6, 9 중 하나라면 -로 변경한다.
#todo 카운트 함수를 활용한다.
n = int(input())
for i in range(1,n+1):
    i = str(i)
    c = i.count('3') + i.count('6') + i.count('9')
    if c == 0:
        print(i, end=' ')
    else:
        print('-'*c, end=' ')

#? 어째서 str인데 리스트 메소드인 .count를 쓸 수 있는거지?
#! i.count('x')는 그 시퀀스에 해당 값이 몇 개인지 알려주는 정수값이다. 고로 + 산술 연산자 사용 가능 

#! 문자열*수 = 문자열 반복해주는 것 잊지 말기

# N = int(input())
# clap = ['3', '6', '9']

# for i in range(1, N+1):
#     count = 0
#     for j in str(i):
#         if j in clap:
#             count += 1
#     if count > 0:
#         i = '-' * count
#     print(i, end=' ')
