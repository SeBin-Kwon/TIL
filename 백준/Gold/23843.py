import sys
import heapq
sys.stdin = open('23843.txt', 'r')
input = sys.stdin.readline

n, m = map(int,input().split())
# 전자기기
e = []
heapq.heapify(e)
for i in map(int,input().split()):
    heapq.heappush(e,-i)
# [-8, -4, -4, -1, -1]
# 콘센트
c = []
heapq.heapify(c)

# 전자기기 다 빠질 때 까지
while e:
    if len(c) < m:
        heapq.heappush(c,-heapq.heappop(e))
    # 콘센트 꽉차면
    else:
        min_ = heapq.heappop(c)
        d = -heapq.heappop(e)
        heapq.heappush(c, min_ + d)
print(max(c))

