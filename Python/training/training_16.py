# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지
# 비교해서 카운트 / 만약 문자열에 모음이 있다면

word = input()
m = ['a', 'e', 'i', 'o', 'u']
cnt = 0
for i in word:
    for j in m:
        if i == j:
            cnt += 1
print(cnt)