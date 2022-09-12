import sys
import heapq
input = sys.stdin.readline
heap = []
n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
            
        else:
            print(0)
            
    else:
        heapq.heappush(heap,-x)