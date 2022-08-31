import sys
sys.stdin = open('1966.txt', 'r')

# from collections import deque

T = int(input())
for t in range(T):
    n, m = map(int,input().split()) # 문서 개수, 출력할 문서 위치
    queue = list(map(int,input().split())) # 문서 중요도
    # queue = deque()
    sorted(queue)