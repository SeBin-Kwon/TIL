from  collections import deque
import sys
# sys.stdin = open('1260.txt', 'r')
input = sys.stdin.readline

n, m, v = map(int,input().split())

#todo 인접 리스트 생성
# 간선 개수 만큼 리스트요소 생성하고 그 안에 정점들을 인덱스에 맞게 배치
#! 1부터 시작하기 때문에 n+1을 한다.
g = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

#? 방문할 수 있는 정점이 여러 개인 경우 번호 작은 것부터 방문 (1번 ~ N번)
# 정점들을 오름차순으로 정렬
for i in range(1,n+1):
    g[i].sort()

#todo 방문 리스트 생성 (n+1 잊지 않는다)
visited = [0] * (n+1)

# v부터 방문 시작
def dfs(v):
    #! 방문한 정점 프린트하기
    print(v,end=' ')

    # 방문 리스트에 표시
    visited[v] = 1

    # 인덱스로 접근 후 인접한 정점 체크
    for i in g[v]:
        # 만약 방문하지 않았다면
        if not visited[i]:
            # 방문 체크하고
            visited[i] = 1
            # 다시 dfs 함수 호출
            dfs(i)

def bfs(v):
    # v가 담긴 리스트로 덱 생성
    queue = deque([v])
    # 방문 체크
    visited[v] = 1

    # 큐가 참이라면 / 정점이 들어있다면
    while queue:
        # 큐에 담긴 요소 팝해서 빼기 / 현재 있는 곳
        now = queue.popleft()
        #! 방문한 정점 프린트
        print(now,end=' ')

        # 현재 있는 곳과 인접한 정점 체크
        for i in g[now]:
            # 방문하지 않았다면
            if not visited[i]:
                # 방문 체크하고
                visited[i] = 1
                # 큐에 추가
                queue.append(i)

# dfs 함수 호출
dfs(v)
# 개행 하기
print()

# dfs로 쓰인 방문 리스트 초기화 해주기
visited = [0] * (n+1)
# bfs 함수 호출
bfs(v)