n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
answer = []

def backtracking(idx):
    if len(answer) == m:
        print(*answer)
        return
    for i in range(idx, n):
        answer.append(nums[i])
        backtracking(i)
        answer.pop()
backtracking(0)