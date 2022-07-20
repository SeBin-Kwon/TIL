t = int(input())
for test_case in range(1,t+1):
    a, b = map(int, input().split())
    i = a//b
    j = a%b
    print(f'#{test_case}', i, j)
