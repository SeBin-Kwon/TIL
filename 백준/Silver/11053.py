import sys
sys.stdin = open('11053.txt', 'r')
input = sys.stdin.readline

n = int(input())
array = list(map(int,input().split()))

dp = [1] * n

for i in range(1,n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))