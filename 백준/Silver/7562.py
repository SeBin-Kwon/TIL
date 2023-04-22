import sys
from collections import deque
sys.stdin = open('7562.txt','r')
input = sys.stdin.readline

T = int(input())
for t in range(T):
    l = int(input())
    board = [[0] * l for _ in range(l)]
    cx, cy = map(int, input().split())
    mx, my = map(int, input().split())
    
