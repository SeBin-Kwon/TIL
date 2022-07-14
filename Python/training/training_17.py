# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지
# 소문자 아스키코드 숫자로 바꾸고 -32 해준뒤 문자로 반환
word = input()
up = ''
for i in word:
    c = ord(i) - 32
    up += chr(c)
print(up)

