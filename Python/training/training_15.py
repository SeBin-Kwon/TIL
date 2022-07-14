# 문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
# a 가 없는 경우에는 -1을 출력해주세요.
# find() index() 메서드 사용 금지
# 일단 a인지 아닌지 확인하고 만약 a라면
# 레인지로 수열 만들고 그 숫자를 인덱싱해서 만약 a리면 그 숫자 출력

word = input()
for i in range(len(word)):
    if word[i] == 'a':
        print(i)
        break
    else:
        print(-1)
        break

# 추가 문제
# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지
word = input()
for i in range(len(word)):
    if word[i] == 'a':
        print(i, end=' ')
        
    
