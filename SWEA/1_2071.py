t = int(input())
for test_case in range(1,t+1):
    a = map(int, input().split())
    avg = round(sum(a)/10)
    print(f'#{test_case}', avg)