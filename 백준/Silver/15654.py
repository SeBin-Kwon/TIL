import sys
from itertools import permutations
sys.stdin = open('15654.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

print('\n'.join(map(' '.join, permutations(map(str, nums), m))))

# for i in permutations(nums, m):
#     print(*i)