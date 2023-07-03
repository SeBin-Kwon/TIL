from collections import defaultdict
from collections import deque


def get_result(x, k):
    if k == 'D':
        return (x*2) % 10000
    if k == 'S':
        return x-1 if x != 0 else 9999
    if k == 'L':
        return (x % 1000)*10 + x//1000
    if k == 'R':
        return (x % 10)*1000 + x//10


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    dict = defaultdict(str)
    dict[a] = ''
    q = deque()
    q.append(a)
    while q:
        x = q.popleft()
        if x == b:
            break
        for k in ['D', 'S', 'L', 'R']:
            result = get_result(x, k)
            if result not in dict:
                q.append(result)
                dict[result] = dict[x] + k
    print(dict[b])