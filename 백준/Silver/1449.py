import sys
sys.stdin = open('1449.txt', 'r')
input = sys.stdin.readline

n,l = map(int,input().split())
pipe = list(map(int,input().split()))
# 입력이 정렬해서 주어지지 않기 때문에 정렬해준다.
pipe.sort()

# 물 새는 곳 1개 이상 주어지기 때문에 cnt는 1로 시작
cnt = 1
# 테이프 끝나는 곳을 저장
end = pipe[0]+l

for i in range(n):
    # 해당 구멍이 테이프 안에 포함된다면 1개로 다 막을 수 있는 것이므로 continue
    if pipe[i] < end:
        continue
    # 테이프 길이를 벗어난다면
    else:
        # 해당 지점을 기준으로 테이프 끝나는 곳을 새로 저장, 새 테이프 사용
        end = pipe[i]+l
        # 테이프 개수 늘리기
        cnt += 1
print(cnt)

# 처음엔 이 위치들의 차이를 이용해서 풀려고 했더니 잘 안됬고
# 단순히 위치가 아니라 숫자로 봐서 숫자들의 범위로 바라봐야 풀렸다.
    # len_ = 0
    # len_ += abs(pipe[i] - pipe[i+1])
    # if len_ <= l:
    #     cnt += 1
    # else:
    #     continue