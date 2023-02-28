import sys
sys.stdin = open('1992.txt', 'r')
input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]

def quadtree(x, y, n):
    check = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != check:
                print('(', end='')
                quadtree(x, y, n//2)
                quadtree(x, y+n//2, n//2)
                quadtree(x+n//2, y, n//2)
                quadtree(x+n//2, y+n//2, n//2)
                print(')', end='')
                return

    print(1 if check == '1' else '0', end='')

quadtree(0, 0, n)