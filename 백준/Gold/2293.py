import sys
sys.stdin = open('2293.txt','r')
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
case_ = []
cnt = 0
