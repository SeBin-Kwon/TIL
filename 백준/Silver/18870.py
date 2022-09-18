import sys
sys.stdin = open('18870.txt','r')

n = int(input())
nums = list(map(int,input().split()))

s_nums = sorted(set(nums))

cnt = 0
dic = {}
for i in s_nums:
    dic[i] = cnt
    cnt += 1

result = []
for i in range(n):
    result.append(dic[nums[i]])

print(*result)