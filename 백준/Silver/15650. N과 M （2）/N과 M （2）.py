from itertools import combinations
n, m = map(int, input().split())
nums = [i for i in range(1,n+1)]
for items in combinations(nums, m):
    for j in items:
        print(j, end=' ')
    print()