import sys
sys.stdin = open('11945.txt','r')

N, M = map(int, input().split())
for _ in range(N):
    print(input()[::-1])    