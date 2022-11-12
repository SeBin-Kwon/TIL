import sys
sys.stdin = open('17144.txt', 'r')
input = sys.stdin.readline

r, c, t = map(int,input().split())

room = [list(map(int,input().split())) for i in range(r)]


