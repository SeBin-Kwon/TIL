import sys
sys.stdin = open('16928.txt', 'r')
input = sys.stdin.readline

# 주사위 1 ~ 6
# 게임 10 x 10, 100개의 칸
# 주사위 굴린 결과 > 100은 안됨
# 도착한 칸 : 사다리 => 앞, 뱀 => 뒤
# 도착한 칸 == 100이 되기 위해 주사위 굴리는 최소 횟수
# n : 사다리의 수, m : 뱀의 수 

n, m = map(int, input().split())
ladder = []
for _ in range(n):
    ladder.append(tuple(map(int, input().split())))
snake = []
for _ in range(m):
    snake.append(tuple(map(int, input().split())))

ladder.sort()
cnt = 0
board = 0
for i in range(1, 7):
    if i != ladder[1]:
        board += i
print(ladder)
# 주사위를 사다리나 뱀 나올 때 까지 굴려 1 ~ 6
# 나오면 횟수 카운트 더해주기
# 사다리와 뱀들이 연결되어 있다면 bfs
# bfs 끝나면 횟수 카운트