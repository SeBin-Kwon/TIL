# 1~6까지 주사위 3개
# 같은눈 3개 : 10,000원+(같은 눈)×1,000원
# 같은눈 2개 : 1,000원+(같은 눈)×100원
# 같은눈 없음 : (그 중 가장 큰 눈)×100원


a, b, c = map(int,input().split())
if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max(a, b, c) * 100)
