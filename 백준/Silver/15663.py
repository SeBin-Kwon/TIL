import sys
sys.stdin = open('15663.txt', 'r')
input = sys.stdin.readline
#! 백트래킹 dfs
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
answer = []
visited = [0] * n
def dfs():
    if len(answer) == m:
        print(*answer)
        return
    remember = 0
    for i in range(0, n):
        if not visited[i] and remember != nums[i]:
            answer.append(nums[i])
            visited[i] = 1
            remember = nums[i]
            dfs()
            visited[i] = 0
            answer.pop()
dfs()

            