# 지점 n개, 출발 지점 s, a도착, b도착
# 간선 사이 요금, 방향별로 요금 달라지지 않음
# 합승하지 않아도 됨.
# 최저 택시 요금 합산해서 계산
#? 다익스트라, 플로이드 워셜
# 시작지점 -> 마지막 합승 시점, 마지막 합승 시점 -> A or B
# 마지막 합승 시점은 모든 노드에서 구하기
n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]


import heapq

def dijkstra(start):
    return

def solution(n, s, a, b, fares):
    answer = 0
    INF = 1e8
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    distance = [INF] * (n+1)

    for i in fares:
        graph[i[0]].append((i[2], i[1]))

    dijkstra(s)
    return answer


print(solution(n, s, a, b, fares))