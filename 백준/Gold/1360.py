import sys
sys.stdin = open('1360.txt','r')
input = sys.stdin.readline

n = int(input())
cmd = [list(input().split()) for i in range(n)]
