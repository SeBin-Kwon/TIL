import sys

sys.stdin = open("input.txt", "r")

t = int(input())
result = 0
for test_case in range(1,t+1):
    a = max(map(int, input().split()))
    print(f'#{test_case}', a)