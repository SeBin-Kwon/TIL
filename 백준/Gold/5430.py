import sys
from collections import deque
sys.stdin = open('5430.txt','r')
input = sys.stdin.readline

T = int(input())
for t in range(T):
    p = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))

    if n == 0:
        arr = []
    
    flag = True
    for i in p:
        if i == 'R':
            flag = not flag
        else:
            if arr:
                if not flag:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print('error')
                break
    else:
        if not flag:
            arr.reverse()
            print(f'[{",".join(arr)}]')
        else:
            print(f'[{",".join(arr)}]')
