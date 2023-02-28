import sys
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