# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
word = 'apple'
r = ''
# 1. for
# for i in word:
#     r = i + r
# print(r)

# 2. pythonic
# print(word[::-1])
#print(''.join(reversed(word)))

# 3. index
for i in range(len(word)):
    print(word[len(word)-i-1])