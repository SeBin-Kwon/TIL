import sys
from collections import deque
sys.stdin = open('9019.txt', 'r')
input = sys.stdin.readline

# a를 b로 바꾸는 최소 명령어 생성
#* 숫자들이 같으면 L or R
#* D는 *2, S는 -1
# 1, 2, 3, 4번 연산 각각 식으로 정리해서 그대로 bfs적용하면 됩니다.
#! bfs는 기본적으로 가중치가 모두 같을 때 최단경로 보장 -> 1, 2, 3, 4번 연산 모두 가중치가 같다고 볼 수 있음 -> 고로 bfs적용 가능.
#? 다만 연산별로 어떤 조건을 만족해야 하는지 잘 고려해야함.(+자릿수에 0이 포함된 경우)
#? 그리고 방문처리에 있어서 기존의 bfs는 bool이나 방문번째를 기록하거나 했는데
#! 이 문제에선 "문자열"을 기록해야함.
#? 이후 Visit[B]가 곧 답.

#* 문자열로 변환하고 다시 정수형을 변환하는 과정에서 시간이 걸림

def D(a):
    result_D = a * 2
    if result_D > 9999:
        result_D %= 10000
    return result_D

def S(a):
    result_S = a - 1
    if result_S == -1:
        result_S = 9999
    return result_S

def L(a): # 1234 -> 2341
    front_a = a % 1000
    back_a = a // 1000
    result_L = front_a * 10 + back_a
    return result_L

def R(a): # 1234 -> 4123
    front_a = a % 10
    back_a = a // 10
    result_R = front_a * 1000 + back_a
    return result_R


def bfs(a, b):
    queue = deque([a])
    while queue:
        queue.append(1)

visited = ''

T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    bfs(a, b)


# from collections import defaultdict
# from collections import deque


# def get_result(x, k):
#     if k == 'D':
#         return (x*2) % 10000
#     if k == 'S':
#         return x-1 if x != 0 else 9999
#     if k == 'L':
#         return (x % 1000)*10 + x//1000
#     if k == 'R':
#         return (x % 10)*1000 + x//10


# T = int(input())
# for _ in range(T):
#     a, b = map(int, input().split())
#     dict = defaultdict(str)
#     dict[a] = ''
#     q = deque()
#     q.append(a)
#     while q:
#         x = q.popleft()
#         if x == b:
#             break
#         for k in ['D', 'S', 'L', 'R']:
#             result = get_result(x, k)
#             if result not in dict:
#                 q.append(result)
#                 dict[result] = dict[x] + k
#     print(dict[b])

# T = int(input())
# inst = ['D', 'S', 'L', 'R']
# for _ in range(T):
#     x, y = map(int, input().split())
#     change = [False] * 10000
#     prev = [False] * 10000
#     que = deque([x])
#     change[x] = 'X'
#     while que:
#         x = que.popleft()
#         next = []
#         next.append((2*x)%10000)
#         next.append((x+9999)%10000)
#         next.append((x//1000)+((x*10)%10000))
#         next.append((x//10)+((x%10)*1000))
#         for i in range(4):
#             if not change[next[i]]:
#                 change[next[i]] = inst[i]
#                 prev[next[i]] = x
#                 que.append(next[i])
#             if next[i] == y:
#                 que = []
#                 break
    
#     result = []
#     while change[y] != 'X':
#         result.append(change[y])
#         y = prev[y]
#     result.reverse()
#     print("".join(result))