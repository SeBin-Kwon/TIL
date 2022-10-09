import sys
sys.stdin = open('2847.txt', 'r')
input = sys.stdin.readline

n = int(input())
level = []
for i in range(n):
    level.append(int(input()))

cnt = 0

# 레벨 높은 순으로 반복, 뒤에서 두번째부터 시작
for i in range(n-2,-1,-1):
    # 레벨이 높은게 낮은 것보다 점수가 같거나 작다면
    if level[i+1] <= level[i]:
        # 현재 점수 - 원래 점수(한단계 높은 레벨에서 1을 뺀 값) = 차이 == 카운트
        cnt += level[i] - (level[i+1] - 1)
        # 원래 점수 반영
        level[i] = level[i+1] - 1
print(cnt)
