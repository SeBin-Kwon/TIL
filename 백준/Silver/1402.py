import sys
sys.stdin = open('1402.txt', 'r')
input = sys.stdin.readline

T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    print('yes')