import sys
input = sys.stdin.readline

n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int,input().split())))

def divide(x, y, n):
    global minus, zero, plus
    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                for k in range(3):
                    for l in range(3):
                        divide(x + k * n // 3, y + l * n // 3, n // 3)
                return
    if check == -1:
        minus += 1
    elif check == 0:
        zero += 1
    else:
        plus += 1

minus, zero, plus = 0, 0, 0
divide(0, 0, n)
print(minus, zero, plus, sep="\n")