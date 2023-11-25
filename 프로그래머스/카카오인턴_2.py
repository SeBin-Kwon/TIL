# 그래프 종류별 수 구하기
#! dfs

# edges = [[2,3],[4,3],[1,1],[2,1]]
# edges = [[4,11],[1,12],[8,3],[12,7], [4,2], [7,11], [4,8], [9,6], [10,11],[6,10],[3,5],[11,1],[5,3],[11,9],[3,8]]
edges = [[2,3],[4,3],[1,5],[5,6],[6,1],[2,1], [2,7],[7,8],[8,6]]

def solution(edges):
    answer = []
    n = len(edges)
    donut, stick, eight = 0, 0, 0
    v = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])

    l = list(map(len, graph))
    first = l.index(max(l))
    answer.append(first)

    for start in graph[first]:
        stack = [start]
        v[start] = 1
        spot = []
        while stack:
            cur = stack.pop() 
            for i in graph[cur]:
                if v[i] == 0:
                    v[i] += 1
                    stack.append(i)
                else:
                    v[i] += 1
                    spot.append(v[i])
        if len(spot) == 1:
            donut += 1
        elif len(spot) > 1:
            eight += 1
        elif not spot:
            stick += 1

    answer += [donut, stick, eight]
    return answer

print(solution(edges))