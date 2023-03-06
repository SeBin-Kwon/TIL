import sys
sys.stdin = open('14465.txt', 'r')
input = sys.stdin.readline

n, k, b = map(int, input().split())
broken = [0 for _ in range(n+1)]

for _ in range(b):
    broken[int(input())] = 1

for i in range(1, n+1):
    broken[i] += broken[i-1]

answer = b
for i in range(k, n+1):
    answer = min(answer, broken[i] - broken[i-k])
print(answer)