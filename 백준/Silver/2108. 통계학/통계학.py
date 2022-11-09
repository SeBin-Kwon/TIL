import sys
input = sys.stdin.readline
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
nums.sort()

print(round(sum(nums) / n))
print(nums[n // 2])

mode = dict()
for i in range(1,n+1):
	mode[i] = []

maxcnt = 1
cnt = 1
for i in range(1,n):
    if nums[i] == nums[i-1]:
        cnt += 1
    else:
        mode[cnt].append(nums[i-1])
        if maxcnt < cnt:
            maxcnt = cnt
        cnt = 1
    if i == n-1: 
        mode[cnt].append(nums[i])
        if maxcnt < cnt:
            maxcnt = cnt
if n == 1:
    mode[1].append(nums[0])

mode[maxcnt].sort()
if len(mode[maxcnt]) == 1:
    print(mode[maxcnt][0])
else :
	print(mode[maxcnt][1])

print(nums[-1] - nums[0])