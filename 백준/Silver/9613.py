import sys
sys.stdin = open('9613.txt', 'r')
input = sys.stdin.readline

T = int(input())
for t in range(T):
    nums = list(map(int, input().split()))
    