n, x = map(int, input().split())
a = map(int, input().split())
for i in a:
    if i < x:
        print(i, end=' ')

# Todo 수열 a 중에 x 보다 작은 수를 입력하기
# a를 반복문 돌려서 x와 비교 후 프린트 