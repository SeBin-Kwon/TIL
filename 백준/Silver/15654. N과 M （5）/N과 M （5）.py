import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

print('\n'.join(map(' '.join, permutations(map(str, nums), m))))