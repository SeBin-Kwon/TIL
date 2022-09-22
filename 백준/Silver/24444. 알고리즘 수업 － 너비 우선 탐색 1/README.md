# [Silver II] 알고리즘 수업 - 너비 우선 탐색 1 - 24444 

[문제 링크](https://www.acmicpc.net/problem/24444) 

### 성능 요약

메모리: 59600 KB, 시간: 656 ms

### 분류

너비 우선 탐색(bfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal), 정렬(sorting)

### 문제 설명

<p>오늘도 서준이는 너비 우선 탐색(BFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.</p>

<p><em>N</em>개의 정점과 <em>M</em>개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 <em>N</em>번이고 모든 간선의 가중치는 1이다. 정점 <i>R</i>에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.</p>

<p>너비 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 <strong>오름차순</strong>으로 방문한다.</p>

<pre>bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    for each v ∈ V - {R}
        visited[v] <- NO;
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
    while (Q ≠ ∅) {
        u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
        for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 <strong>오름차순</strong>으로 방문한다)
            if (visited[v] = NO) then {
                visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
                enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
            }
    }
}</pre>

### 입력 

 <p>첫째 줄에 정점의 수 <em>N</em> (5 ≤ <em>N</em> ≤ 100,000), 간선의 수 <em>M</em> (1 ≤ <em>M</em> ≤ 200,000), 시작 정점 <em>R</em> (1 ≤ <em>R</em> ≤ <em>N</em>)이 주어진다.</p>

<p>다음 <em>M</em>개 줄에 간선 정보 <code><em>u</em> <em>v</em></code>가 주어지며 정점 <em>u</em>와 정점 <em>v</em>의 가중치 1인 양방향 간선을 나타낸다. (1 ≤ <em>u</em> < <em>v</em> ≤ <em>N</em>, <em>u</em> ≠ <em>v</em>) 모든 간선의 (<em>u</em>, <em>v</em>) 쌍의 값은 서로 다르다.</p>

### 출력 

 <p>첫째 줄부터 <em>N</em>개의 줄에 정수를 한 개씩 출력한다. <em>i</em>번째 줄에는 정점 <em>i</em>의 방문 순서를 출력한다. 시작 정점의 방문 순서는 1이다. 시작 정점에서 방문할 수 없는 경우 0을 출력한다.</p>

