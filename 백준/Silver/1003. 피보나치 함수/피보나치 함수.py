import sys

input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    zero, one = 1, 0
    for i in range(n):
        zero, one = one, zero + one
    print(zero, one)