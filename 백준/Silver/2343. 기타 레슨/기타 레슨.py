import sys
input = sys.stdin.readline

n, m = map(int,input().split())
l = list(map(int,input().split()))
left, right = max(l), sum(l)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    time = 0
    for i in range(n):
        if time + l[i] > mid:
            cnt += 1
            time = 0
        time += l[i]
    if time:
        cnt += 1

    if cnt <= m:
        right = mid - 1
    else:
        left = mid + 1
print(left)