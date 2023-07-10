import sys
input = sys.stdin.readline

def back(x):
    if len(answer) == m:
        print(*answer)
        return

    for i in range(x, n+1):
        answer.append(i)
        back(i)
        answer.pop()

n, m = map(int, input().split())
answer = []
back(1)