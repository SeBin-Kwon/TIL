import sys
from collections import deque
sys.stdin = open('7569.txt','r')
input = sys.stdin.readline

# 익은 토마토와 인접한 토마토는 익음
# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향
# 며칠 지나면 모두 익는지 최소 일수 구하기

m, n, h = map(int, input())
graph = [list(map(int, input())) for _ in range(n)]
