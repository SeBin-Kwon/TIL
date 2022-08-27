from collections import deque

def solution(progresses, speeds):
    answer = []
    t = 1 
    cnt = 0

    p = deque(progresses)
    s = deque(speeds)

    while p:

        if p[0] + (s[0] * t) < 100:
            t += 1
            if cnt:
                answer.append(cnt)
                cnt = 0

        elif p[0] + (s[0] * t) >= 100:
            p.popleft()
            s.popleft()
            cnt += 1

    answer.append(cnt)
    return answer
