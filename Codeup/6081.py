n = int(input(),16)
for i in range(1,16):
    print('%X'%n,'*%X'%i,'=%X'%(n*i),sep='')
# int()의 2번째 인자는 디폴트 값이 10이기 때문에 10진수의 숫자로 변환한다.
# 따라서 다른 진수의 숫자로 변환하려면 진수 base 값에 추가 인자를 넘겨준다.