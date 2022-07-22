n = input()
# while True: # 종료조건은 n과 결과값이 같을 경우
# 문자열 인덱스 인트 변환 게산
n1 = n
a = 0
cnt = 0
new_num = ''
stop = 0
while True:
    cnt += 1
    if int(n) < 10:
        n = '0' + n
    for i in n:
        a += int(i)
        s = str(a)
    print(s)
    new_num = n[1]+ s
    n = new_num
    print('새로운수',new_num)
    if n1 == new_num:
        break
    stop += 1
    if stop > 10:
        break
    

