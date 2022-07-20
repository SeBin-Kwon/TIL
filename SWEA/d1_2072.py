import sys

sys.stdin = open("input.txt", "r")

t = int(input())
result = 0
for test_case in range(1,t+1):
    a = map(int, input().split())
    for i in a:
        if i % 2 != 0:
            result += i
    print(f'#{test_case}', result)
    result = 0