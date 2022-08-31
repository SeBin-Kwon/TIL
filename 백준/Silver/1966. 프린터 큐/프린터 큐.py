import sys
from collections import deque
T = int(input())
for t in range(T):
    n, m = map(int,input().split()) # 문서 개수, 출력할 문서 위치
    queue = deque(list(map(int,input().split()))) # 문서 중요도
    cnt = 0
    position = deque([0 for _ in range(n)])
    position[m] = 1

    while queue:
        if queue[0] != max(queue):
            queue.append(queue.popleft())
            position.append(position.popleft())
        else:
            cnt += 1
            if position[0] == 1:
                print(cnt)
                break
            else:
                queue.popleft()
                position.popleft()