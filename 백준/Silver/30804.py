import sys
sys.stdin = open('30804.txt', 'r')
input = sys.stdin.readline

N = int(input())
S = tuple(map(int, input().split()))
res = i = 0
cnt_list = [0]*10
current = set()
for j in range(N):
    cnt_list[S[j]] += 1
    current.add(S[j])
    if len(current) > 2:
        while 1:
            cnt_list[S[i]] -= 1
            if cnt_list[S[i]] == 0:
                current.remove(S[i])
                i += 1
                break
            i += 1
    if j-i+1 > res:
        res = j-i+1
print(res)
    
# def two_pointer(arr, left, right, cnt, kind, max_len, nums, N):
#     if right >= N:
#         return max_len

#     if nums[arr[right]] == 0:
#         kind += 1

#     cnt += 1
#     nums[arr[right]] += 1

#     if kind > 2:
#         if nums[arr[left]] == 1:
#             kind -= 1
#         nums[arr[left]] -= 1
#         cnt -= 1
#         left += 1

#     max_len = max(max_len, cnt)

#     return two_pointer(arr, left, right + 1, cnt, kind, max_len, nums, N)

# N = int(input().strip())
# arr = list(map(int, input().strip().split()))

# nums = [0] * (max(arr) + 1)
# print(two_pointer(arr, 0, 0, 0, 0, 0, nums, N))