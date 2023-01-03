import sys

input = sys.stdin.readline

zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(n):
    length = len(zero)
    if n >= length:
        for i in range(length, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[n], one[n])
T = int(input())
for t in range(T):
    n = int(input())
    fibonacci(n)