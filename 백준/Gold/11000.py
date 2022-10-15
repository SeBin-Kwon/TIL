import sys

sys.stdin = open('11000.txt', 'r')
input = sys.stdin.readline

n = int(input())
lecture = []
for i in range(n):
    lecture.append(list(map(int,input().split())))
lecture.sort()

cnt = 0
for i in range(n-1):
    if lecture[i][1] <= lecture[i+1][0]:
        continue
    else:
        cnt += 1
    print(lecture)
    print(cnt)
