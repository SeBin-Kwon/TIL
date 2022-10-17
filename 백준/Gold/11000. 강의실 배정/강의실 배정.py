import sys
import heapq
input = sys.stdin.readline

n = int(input())
lecture = []
for i in range(n):
    lecture.append(list(map(int,input().split())))
lecture.sort()

room = []
heapq.heappush(room, lecture[0][1])

for i in range(1, n):
    if lecture[i][0] < room[0]:
        heapq.heappush(room, lecture[i][1])
        continue
    else:
        heapq.heappop(room)
        heapq.heappush(room, lecture[i][1])
print(len(room))