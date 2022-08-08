t = int(input()) # 테스트 케이스

for _ in range(t):
    s = int(input()) # 자동차 가격
    n = int(input()) # 옵션 개수
    sum_ = 0
    for _ in range(n):
        q, p = map(int,input().split()) # 사려는 옵션 개수, 가격
        sum_ += q*p
    sum_ += s
    print(sum_)