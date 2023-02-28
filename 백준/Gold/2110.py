import sys
sys.stdin = open('2110.txt','r')
input = sys.stdin.readline

n, c = map(int,input().split())
houses = [int(input()) for i in range(n)]
houses.sort()

# 최소거리와 최대거리
start = 1
end = houses[-1] - houses[0]

def binarySearch(houses, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 앞에서부터 탐색
        current = houses[0]
        cnt = 1
        for i in range(1,n):
            # 현재 위치에서 다음 집과의 거리가 mid 이상이라면
            if houses[i] >= current + mid:
                # 공유기 개수 + 1
                cnt += 1
                # 현재 위치 갱신
                current = houses[i]
        if cnt >= c:
            # cnt가 c 이상이면 더 넓게 설치 가능함
            start = mid + 1
            result = mid
        else:
            # c 미만이면 더 좁게 설치 해야함
            end = mid - 1
    return result

print(binarySearch(houses, start, end))
    