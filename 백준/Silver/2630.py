import sys
sys.stdin = open('2630.txt', 'r')
input = sys.stdin.readline

n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int,input().split())))
result = [0, 0] # 흰 종이, 파란 종이

#! 절반 나눈 만큼 x,y의 시작지점이 늘어난다.
def divide(x,y,n):
    color = paper[x][y] # 비교할 색 저장
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != paper[i][j]: # 색이 다르면 나누기
                divide(x, y, n//2)
                divide(x, y+n//2, n//2)
                divide(x+n//2, y, n//2)
                divide(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1

divide(0,0,n)
print(result[0])
print(result[1])
