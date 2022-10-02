import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
		# set으로 중복 제거
    one = set(map(int,input().split()))
    m = int(input())
    two = list(map(int,input().split()))
		
		# 두번째 수첩의 숫자가 첫번째 수첩에 있으면
    for i in range(m):
        if two[i] in one:
            print(1)
        else:
            print(0)
