import sys
from itertools import combinations
sys.stdin = open('14889.txt', 'r')
input = sys.stdin.readline


n = int(input())
members = [ i for i in range(n)]

stat = []
for i in range(n):
    stat.append(list(map(int,input().split())))

team =list(combinations(members, n//2))

link = 0
for m in team[:n//2+1]:
    start = 0
    for j in m:
        start 
# for i in team[n//2+1:]:
#     print(i)
