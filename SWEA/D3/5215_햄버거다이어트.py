import sys
from itertools import combinations
sys.stdin = open('5215_햄버거다이어트.txt','r')
input = sys.stdin.readline

T = int(input())
for a in range(1,T+1):
    n, l = map(int,input().split())
    element = []
    for i in range(n):
        t, k  = map(int,input().split())
        element.append((t,k))
    max_score = 0
    for i in range(1, n+1):
        for j in combinations(element, i):
            score = 0
            cal = 0
            for r in range(len(j)):
                score += j[r][0]
                cal += j[r][1]
            if cal > l:
                continue
            if max_score < score:
                max_score = score

    print(f'#{a} {max_score}')