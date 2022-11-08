import sys
from itertools import permutations
input = sys.stdin.readline



n, m = map(int,input().split())

nums = []
for i in range(1,n+1):
    nums.append(i)
result = list(permutations(nums, m))

for i in result:
    print(*i)