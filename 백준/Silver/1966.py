import sys
sys.stdin = open('1966.txt', 'r')

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
                
# t = int(input())

# for i in range(t):
#     n, m = map(int, input().split())
#     queue = deque(list(map(int, sys.stdin.readline().split())))
#     count = 0
#     while queue:
#         best = max(queue)  #현재의 최댓값이 가장 먼저 배출되므로 최댓값을 저장
#         front = queue.popleft() # 큐의 front를 뽑았으므로
#         m -= 1 # 내 위치가 한 칸 당겨진다.

#         if best == front: # 뽑은 숫자가 제일 큰 숫자일 때
#             count += 1 # 하나가 영원히 배출되므로 순번 하나 추가
#             if m < 0: # m이 0이라는 것은 뽑은 숫자가 내 숫자라는 뜻.
#                 print(count)
#                 break

#         else:   # 뽑은 숫자가 제일 큰 숫자가 아니면
#             queue.append(front) # 제일 뒤로 밀려나게 됨
#             if m < 0 :  # 제일 앞에서 뽑히면
#                 m = len(queue) - 1 # 제일 뒤로 이동