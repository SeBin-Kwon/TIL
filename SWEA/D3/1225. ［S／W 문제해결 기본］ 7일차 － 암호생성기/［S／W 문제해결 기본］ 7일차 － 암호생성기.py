from collections import deque

T = 10
for tc in range(1, T+1):
    t = int(input())
    n = list(map(int,input().split()))
    n = deque(n)

    while n[-1] != 0:
        for i in range(1,6):
            if n[0] - i > 0:
                n[0] -= i
                n.append(n.popleft())

            elif n[0] - i <= 0:
                n[0] = 0
                n.append(n.popleft())
                break
            
    print(f'#{t}',*n)