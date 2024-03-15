import sys
sys.stdin = open('15666.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
answer = []

def dfs(idx):
    if len(answer) == m:
        print(*answer)
        return
    for i in range(idx,len(nums)):
        answer.append(nums[i])
        dfs(i)
        answer.pop()
dfs(0)
