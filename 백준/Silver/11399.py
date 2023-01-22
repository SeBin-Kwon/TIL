import sys
sys.stdin = open('11399.txt', 'r')
input = sys.stdin.readline

# n = int(input())
# p = list(map(int,input().split()))
# p.sort()
# sum_ = [0] * n
# sum_[0] = p[0]
# for i in range(1, n):
#     sum_[i] += p[i] + sum_[i-1]
# print(sum(sum_))

n = int(input())
p = list(map(int,input().split()))
p.sort()
sum_ = 0
result = 0
for i in p:
    sum_ += i
    result += sum_
print(result)
