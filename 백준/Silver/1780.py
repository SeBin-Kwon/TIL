import sys
sys.stdin = open('1780.txt', 'r')
input = sys.stdin.readline

n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int,input().split())))
result = [0, 0, 0]

def divide(x, y, n):
    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                for k in range(x, x + n, n // 3):
                    for l in range(y, y + n, n // 3):
                        divide(k, l, n // 3)
                return
    result[check + 1] += 1

divide(0, 0, n)
print(*result, sep="\n")