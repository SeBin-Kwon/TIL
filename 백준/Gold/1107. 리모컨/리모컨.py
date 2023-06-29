import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = list(map(int, input().split()))

min_count = abs(100 - n)

for nums in range(1000001):
    nums = str(nums)
    for i in range(len(nums)):
        if int(nums[i]) in broken:
            break
        elif i == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - n) + len(nums))

print(min_count)
