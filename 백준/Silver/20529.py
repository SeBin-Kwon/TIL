import sys
sys.stdin = open('20529.txt', 'r')
input = sys.stdin.readline

#* 비둘기 집 원리

t = int(input())
while t:
    answer = 1e9
    t -= 1
    n = int(input())
    mbti = input().split()
    if n > 32:
        print(0)
    else:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    tmp = 0
                    if i == j or j == k or i == k:
                        continue
                    for x in range(4):
                        if mbti[i][x] != mbti[j][x]:
                            tmp += 1
                        if mbti[j][x] != mbti[k][x]:
                            tmp += 1
                        if mbti[i][x] != mbti[k][x]:
                            tmp += 1
                    answer = min(tmp, answer)
        print(answer)