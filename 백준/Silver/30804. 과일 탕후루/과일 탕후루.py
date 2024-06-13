import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def two_pointer(arr, left, right, cnt, kind, max_len, nums, N):
    if right >= N:
        return max_len

    if nums[arr[right]] == 0:
        kind += 1

    cnt += 1
    nums[arr[right]] += 1

    if kind > 2:
        if nums[arr[left]] == 1:
            kind -= 1
        nums[arr[left]] -= 1
        cnt -= 1
        left += 1

    max_len = max(max_len, cnt)

    return two_pointer(arr, left, right + 1, cnt, kind, max_len, nums, N)

N = int(input().strip())
arr = list(map(int, input().strip().split()))

nums = [0] * (max(arr) + 1)
print(two_pointer(arr, 0, 0, 0, 0, 0, nums, N))