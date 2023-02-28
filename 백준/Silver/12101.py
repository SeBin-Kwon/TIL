import sys
sys.stdin = open('12101.txt', 'r')
input = sys.stdin.readline

def sol(sum_, arr):
    if sum_ == n:
        result.append(arr)
        return
    if sum_ + 1 <= n:
        sol(sum_ + 1, arr + [1])
    if sum_ + 2 <= n:
        sol(sum_ + 2, arr + [2])
    if sum_ + 3 <= n:
        sol(sum_ + 3, arr + [3])

n, k = map(int,input().split())
result = []
sol(0,[])
if k > len(result):
    print(-1)
else:
    result.sort()
    print(*result[k-1], sep='+')