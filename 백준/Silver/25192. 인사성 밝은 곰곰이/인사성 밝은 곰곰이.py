import sys
input = sys.stdin.readline

dict = {}
cnt = 0
N = int(input())

for _ in range(N):
    n = input().strip('\n')
    
    if n == 'ENTER':
        for v in dict.values():
            if v == 1:
                cnt += 1
        dict = {}

    elif n not in dict:
        dict[n] = 1

for v in dict.values():
    if v == 1:
        cnt += 1
print(cnt)