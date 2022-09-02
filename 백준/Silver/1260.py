import sys
from  collections import deque
sys.stdin = open('1260.txt', 'r')

n, m, v = map(int,input().split())
g = [[] * n for _ in range(m)]
