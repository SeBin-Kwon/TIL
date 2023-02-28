# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램
# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M
# 둘째 줄에는 N개의 수
# 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j

import sys
sys.stdin = open('11659.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
sum_ = [0]

temp = 0
for i in nums:
    temp += i
    sum_.append(temp)

for i in range(m):
    a, b = map(int, input().split())
    print(sum_[b] - sum_[a-1])