n = ''
p = 0

while n != '고무오리 디버깅 끝':
    n = input()
    if n == '문제':
        p += 1
    elif n == '고무오리':
        if p != 0:
            p -= 1
        else:
            p += 2
if p > 0:
    print('힝구')
else:
    print('고무오리야 사랑해')