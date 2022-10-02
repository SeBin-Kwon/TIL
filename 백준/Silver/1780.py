import sys
sys.stdin = open('1780.txt', 'r')
input = sys.stdin.readline

n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int,input().split())))

minus = 0
zero = 0
one = 0

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

visited = [[0] * n for _ in range(n)]
