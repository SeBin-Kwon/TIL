# 2단부터 9단까지 반복하여 구구단을 출력하세요.
# * 문자열 출력시 f-string을 활용하면 편하게 작성할 수 있습니다.
num = range(2,10)
num_2 = range(1,10)
for i in num:
    print(f'{i}단')
    for j in num_2:
        print(f'{i} X {j} =', i*j)