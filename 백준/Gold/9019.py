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

def L(a):
    result_L = str(a)[1:]
    result_L += str(a)[0]
    return int(result_L)

def R(a):
    result_R = str(a)[-1]
    result_R += str(a)[:-1]
    return int(result_R)


def bfs(a):
    queue = deque([a])
    while queue:
        queue.append(1)

visited = []

T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    bfs(a)