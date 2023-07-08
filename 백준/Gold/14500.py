import sys
from collections import deque
sys.stdin = open('14500.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())

tetromino = [list(map(int, input().split())) for _ in range(n)]

    