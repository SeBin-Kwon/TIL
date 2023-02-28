import sys
sys.stdin = open('1477.txt','r')
input = sys.stdin.readline

n, m, l = map(int, input().split())
road = [0] + list(map(int, input().split())) + [l]
road.sort()

start = 1
end = l - 1
result = 0
while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in range(n+1):
        if mid < road[i+1] - road[i]:
            cnt += (road[i+1] - road[i]-1) // mid
    if cnt <= m:
        end = mid - 1
        result = mid
    else:
        start = mid + 1
print(result)