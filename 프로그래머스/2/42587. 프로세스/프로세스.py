from collections import deque

def solution(priorities, location):
    queue = deque([])
    answer = 0
    
    for i in enumerate(priorities):
        queue.append(i)
    
    while queue:
        head = queue.popleft()
        if queue and max(queue,key = lambda x: x[1])[1] > head[1]:
            queue.append(head)
        else:
            answer += 1
            if head[0] == location:
                return answer