import sys
sys.stdin = open("1976_input.txt", "r")

# 시간 + 시간 12시간제로
#todo 1시 ~ 12시!

T = int(input())
for test_case in range(1,T+1):
    a = list(map(int,input().split()))
    h = a[0] + a[2]
    m = a[1] + a[3]
    if h > 12:
        h -= 12
    if m > 59:
        m %= 60
        h += 1
    print(f'#{test_case} {h} {m}')
    



    