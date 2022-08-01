import sys
sys.stdin = open('10798.txt','r')

words = []
length = []

for _ in range(5):
    word = input()
    words.append(word)
    length.append(len(word))

result = ''
# 단어의 최대 길이만큼 반복
for i in range(max(length)):
    # 단어 5개
    for j in range(5):
        # 만약 j번째 단어가 최대 길이보다 적을 경우 
        # 건너 뛰기 위한 조건문
        if i < length[j]:
            result += words[j][i]
            # j번째 단어의 i번째 알파벳을 결과값에 추가
print(result)
