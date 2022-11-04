import sys
input = sys.stdin.readline
n = int(input())

def pinary_dp(n):
    pinary = [0, 1, 1]
    for i in range(3, n+1):
        pinary.append(pinary[i-2] + pinary[i-1])
    return pinary[-1]

print(pinary_dp(n))