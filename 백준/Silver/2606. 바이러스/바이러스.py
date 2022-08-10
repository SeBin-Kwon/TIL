n = int(input()) # 정점의 수
m = int(input()) # 간선의 수

com = [[] for _ in range(n+1)]

for i in range(m): # 인접리스트 생성
    c1, c2 = map(int,input().split())
    com[c1].append(c2)
    com[c2].append(c1)

v = [False] * (n+1) # 방문 체크용

stack = [1]
v[1] = True

while stack: # 스택이 비어있지 않다면 계속 반복하기
    virus = stack.pop()

    for j in com[virus]:
        if not v[j]: # 방문하지 않았다면, False라면
            v[j] = True # True로 방문처리
            stack.append(j)
print(sum(v) - 1)