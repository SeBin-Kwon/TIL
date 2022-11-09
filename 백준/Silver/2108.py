import sys
sys.stdin = open('2108.txt', 'r')
input = sys.stdin.readline

#? 산술평균 : N개의 수들의 합을 N으로 나눈 값
#? 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
#? 최빈값 : N개의 수들 중 가장 많이 나타나는 값
#? 범위 : N개의 수들 중 최댓값과 최솟값의 차이

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
# mode = {}
# mode_list = []
# for i in range(n):
#     if num[i] not in mode:
#         mode[num[i]] = 1
#     else:
#         mode[num[i]] += 1

# for i in range(n):
#     if max(mode.values()) == mode[i] and mode.values.count(mode[i]) == 1:
#         mode_ = mode[i]
    # else:
    #     mode_ = max(mode.values())

