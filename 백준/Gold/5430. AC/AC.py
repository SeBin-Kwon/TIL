import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for t in range(T):
    p = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))

    if n == 0:
        arr = []
    
    cnt = 0
    for i in p:
        if i == 'R':
            cnt += 1
        else:
            if arr:
                if cnt % 2 != 0:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print('error')
                break
    else:
        if cnt % 2 != 0:
            arr.reverse()
            print('['+','.join(arr)+']')
        else:
            print('['+','.join(arr)+']')
