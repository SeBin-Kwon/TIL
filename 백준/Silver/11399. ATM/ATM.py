import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))
p.sort()
sum_ = [0] * n
sum_[0] = p[0]
for i in range(1, n):
    sum_[i] += p[i] + sum_[i-1]
print(sum(sum_))