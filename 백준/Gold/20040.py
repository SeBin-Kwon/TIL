import sys
sys.stdin = open('20040.txt','r')
input = sys.stdin.readline

n, m = map(int, input().split())
parents = [i for i in range(n)] #[0,1,2,3,4,5]
result = 0

def find(x):
    # x가 root가 아니라면 재귀로 root를 다시 찾고 갱신한다.
    if x != parents[x]:
        parents[x] = find(parents[x])
        return parents[x]
	# x가 root라면 그대로 반환
    if x == parents[x]:
        return x

def union(x, y, i):
    global result
    # root 찾기
    x = find(x)
    y = find(y)
    # 서로 다른 그룹이라면
    if x != y:
        # 트리를 합친다.
        parents[max(x,y)] = min(x,y)
    elif result == 0:
        result = i

for i in range(m):
    a, b = map(int, input().split())
    union(a, b, i + 1)

print(result)