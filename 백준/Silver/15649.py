import sys
from itertools import permutations
sys.stdin = open('15649.txt', 'r')
input = sys.stdin.readline



# n, m = map(int,input().split())

# nums = []
# for i in range(1,n+1):
#     nums.append(i)
# result = list(permutations(nums, m))

# for i in result:
#     print(*i)

def dfs():
    if len(stack) == m:
        print(*stack)
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = 1
        stack.append(i)
        dfs()
        stack.pop()
        visited[i] = 0

n, m = map(int,input().split())

stack = []
visited = [0] * (n+1)

dfs()

