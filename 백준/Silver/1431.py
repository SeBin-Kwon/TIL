import sys
sys.stdin = open('1431.txt','r')

# 시리얼 번호 순서대로 정렬
#? A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
#todo len 길이 구해서 오름차순 정렬
# 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
#todo 아스키코드표 숫자 48 ~ 57
#? 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
#todo sorted
#! 정렬 순서는 반대로

n = int(input())
s_num = []
for _ in range(n):
    s_num.append(input())

# 사전순 정렬
s_num.sort()

# 자리수 합 딕셔너리에 할당
dic = {}
for i in range(n):
    sum_ = 0
    for j in range(len(s_num[i])):

        # 아스키코드를 이용해서 숫자만 더함
        if 47 < ord(s_num[i][j]) < 58:
            sum_ += int(s_num[i][j])
    dic[s_num[i]] = sum_

s_dic = dict(sorted(dic.items(), key=lambda x: x[1]))

# 길이순 정렬
result = sorted(s_dic, key=len)

print(*result, sep='\n')