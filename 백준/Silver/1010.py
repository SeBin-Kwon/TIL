import sys
sys.stdin = open('1010.txt', 'r')
input = sys.stdin.readline

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

T = int(input())
for t in range(T):
    n, m = map(int,input().split())
    bridge = factorial(m) // (factorial(n) * factorial(m - n))
    print(bridge)
