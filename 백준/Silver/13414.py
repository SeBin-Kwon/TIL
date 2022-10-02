import sys
sys.stdin = open('13414.txt', 'r')
input = sys.stdin.readline

K, L = map(int,input().split())
dic = {}

# 개행문자 없애주고 딕셔너리에 밸류로 순서값을 넣고 저장
for i in range(L):
    dic[input().strip()] = i

# 밸류값(순서)를 기준으로 정렬하여 리스트 형태로 저장
result = sorted(dic.items(), key=lambda x : x[1])
# 수강 가능 인원까지 슬라이싱
# 리스트안 튜플형태로 되어있으므로 튜플의 첫번째 값만 프린트
for i in result[:K]:
    print(i[0])


