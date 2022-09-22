import sys
sys.stdin = open('11650.txt','r')
input = sys.stdin.readline

n = int(input())
for i in range(n):
    x, y = map(int,input().split())
    