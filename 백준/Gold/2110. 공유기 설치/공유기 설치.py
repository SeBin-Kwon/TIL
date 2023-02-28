import sys
input = sys.stdin.readline

n, c = map(int,input().split())
houses = [int(input()) for i in range(n)]
houses.sort()

start = 1
end = houses[-1] - houses[0]

def binarySearch(houses, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = houses[0]
        cnt = 1
        for i in range(1,n):
            if houses[i] >= current + mid:
                cnt += 1
                current = houses[i]
        if cnt >= c:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result

print(binarySearch(houses, start, end))