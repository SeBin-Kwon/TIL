import heapq


def solution(n, s, a, b, fares):
    INF = 10000000
    answer = INF
    graph = [[] * (n + 1) for _ in range(n + 1)]

    for f in fares:
        node1, node2, fee = f
        graph[node1].append((node2, fee))
        graph[node2].append((node1, fee))

    def dijkstra(s):
        q = []
        distance = [INF] * (n + 1)
        heapq.heappush(q, (0, s))
        distance[s] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
                
            for g in graph[now]:
                cost = dist + g[1]
                if cost < distance[g[0]]:
                    distance[g[0]] = cost
                    heapq.heappush(q, (cost, g[0]))
        return distance

    distance_list = [[]] + [dijkstra(i) for i in range(1, n + 1)]

    for i in range(1, n + 1):
        answer = min(distance_list[s][i] + distance_list[i][a] + distance_list[i][b], answer)

    return answer