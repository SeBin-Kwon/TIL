import sys
sys.stdin = open('18111.txt', 'r')
input = sys.stdin.readline

n, m, b = map(int,input().split())
land = [list(map(int,input().split())) for i in range(n)]

time = int(1e9)
height = 0

for target in range(257):
    take_block = 0
    use_block = 0
    for i in range(n):
        for j in range(m):
            if land[i][j] > target:
                take_block += land[i][j] - target
            else:
                use_block += target - land[i][j]
    if use_block > take_block + b:
        continue

    answer = take_block * 2 + use_block
    
    if answer <= time:
        time = answer
        height = target
print(time, height)

