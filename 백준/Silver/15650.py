import sys
sys.stdin = open('15650.txt', 'r')
from itertools import combinations
input = sys.stdin.readline

# 1 ~ n까지 중복없이 자연수 중 m개를 고른 수열
# 고른 수열은 오름차순

n, m = map(int, input().split())
nums = [i for i in range(1,n+1)]
for items in combinations(nums, m):
    print(*items)