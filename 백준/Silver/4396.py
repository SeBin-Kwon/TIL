import sys
sys.stdin = open('4396.txt','r')

from pprint import pprint

n = int(input())
game = [list(input()) for _ in range(n)]
player = [list(input()) for _ in range(n)]
result = [['.'] * n for _ in range(n)]
mine_s = False

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

for i in range(n):
    for j in range(n):
        if player[i][j] == 'x':
            mine_cnt = 0
            for d in range(8):
                nx = dx[d] + i
                ny = dy[d] + j
                if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                    if game[nx][ny] == '*':
                        mine_cnt += 1
            result[i][j] = mine_cnt

            if game[i][j] == '*':
                mine_s = True
if mine_s == True:
    for k in range(n):
        for l in range(n):
            if game[k][l] == '*':
                result[k][l] = '*'

for a in result:
    print(*a,sep='')
