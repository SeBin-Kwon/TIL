import sys

sys.stdin = open("1284_input.txt", "r")

# a : 1리터당 p원
#todo a = w * p
# b : 기본 q원, r리터 이상시 초과량 만큼 1리터당 s원
#todo b = q if w<r else q+(w-r)*s
# 수도양 w리터 작은수 출력

t = int(input())
for test_case in range(1,t+1):
    p,q,r,s,w = map(int,input().split())
    a = w * p
    b = q if w < r else q+(w-r)*s
    print(f'#{test_case} {min(a,b)}')
