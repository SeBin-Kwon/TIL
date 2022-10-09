import sys
input = sys.stdin.readline


def factorial_(n):
    if n > 1:
        return n * factorial_(n - 1)
    else:
        return 1


n = int(input())
print(factorial_(n))
