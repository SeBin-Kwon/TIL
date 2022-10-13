import sys
import heapq
sys.stdin = open('1374.txt', 'r')
input = sys.stdin.readline

n = int(input()) # 강의의 개수

l = []
for i in range(n):
    l.append(list(map(int,input().split())))
heapq.heapify(l)
print(l)