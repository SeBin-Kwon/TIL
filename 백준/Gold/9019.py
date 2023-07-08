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

T = int(input())
dslr = ['D', 'S', 'L', 'R']
for _ in range(T):
    x, y = map(int, input().split())
    command = [False] * 10000
    num = [False] * 10000
    que = deque([x])
    command[x] = 'X'
    while que:
        x = que.popleft()
        next = []
        next.append((2*x)%10000)
        next.append((x+9999)%10000)
        next.append((x//1000)+((x*10)%10000))
        next.append((x//10)+((x%10)*1000))
        for i in range(4):
            if not command[next[i]]:
                command[next[i]] = dslr[i]
                num[next[i]] = x
                que.append(next[i])
            if next[i] == y:
                que = []
                break
    
    result = []
    while command[y] != 'X':
        result.append(command[y])
        y = num[y]
    result.reverse()
    print("".join(result))