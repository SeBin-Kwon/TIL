import sys
sys.stdin = open('1431.txt','r')

# 시리얼 번호 순서대로 정렬
#? A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
#todo len 길이 구해서 오름차순 정렬
# 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
#todo 아스키코드표 숫자 48 ~ 57
#? 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.

n = int(input())
snum = []
for _ in range(n):
    snum.append(input())

# 길이순 정렬
snum.sort(key=len)

# 자리수 합 비교 및 정렬
sum_list = []
for i in range(n):
    sum_ = 0
    for j in range(len(snum[i])):
        if 47 < ord(snum[i][j]) < 58:
            sum_ += int(snum[i][j])
    sum_list.append(sum_)

print(sum_list) 