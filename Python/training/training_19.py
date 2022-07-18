# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

n = int(input())
cnt = 0
while n >= 1 :
    n /= 10
    cnt += 1
print(cnt)
