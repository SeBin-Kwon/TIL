import sys
sys.stdin = open('2805.txt','r')
input = sys.stdin.readline

n, m = map(int,input().split())
tree = list(map(int,input().split()))
tree.sort()
#todo 1을 start 가장 긴 나무 길이를 end
#todo 평균을 mid 전체값 - mid = 벌목 m
#todo while로 옮기면서 값 찾기
#todo end가 절단기

start = 1
end = tree[len(tree)-1]
while start <= end:
    mid = (start + end) // 2
    # 한번 자를 때 마다 초기화 하고 담기
    h = 0
    # 벌목 양 더해주기
    for i in tree:
        if i > mid:
            h += i - mid

    # 목표치 보다 많으면
    if h >= m:
        # 더 안자르게 start값 올리기
        start = mid + 1
    else:
        end = mid - 1

print(end)