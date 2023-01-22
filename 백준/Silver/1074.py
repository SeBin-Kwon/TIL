import sys
sys.stdin = open('1034.txt', 'r')
input = sys.stdin.readline

n, r, c = map(int,input().spilt())
cnt = 0

def solution(n, r, c):
    global cnt
    if n == 0:
        return
    if r 