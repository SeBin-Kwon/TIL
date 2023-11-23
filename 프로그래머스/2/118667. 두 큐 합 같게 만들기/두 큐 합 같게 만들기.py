from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_1, sum_2 = sum(queue1), sum(queue2)
    sum_ = sum_1 + sum_2
    if sum_%2 != 0:
        return -1
    goal = sum_//2
    limit = len(queue1) + len(queue2) + 10
    cnt = 0
    while sum_1 != goal:
        if cnt >= limit:
            return -1
        elif sum_1 < goal:
            pop_ = queue2.popleft()
            sum_1 += pop_
            sum_2 -= pop_
            queue1.append(pop_)
        elif sum_1 > goal:
            pop_ = queue1.popleft()
            sum_1 -= pop_
            sum_2 += pop_
            queue2.append(pop_)
        cnt += 1

    return cnt