import sys
sys.stdin = open('1138.txt', 'r')
input = sys.stdin.readline

n = int(input())
people = list(map(int,input().split()))[::-1]
answer = []
for i in people:
    answer.insert(i,n)
    n -= 1
print(*answer)


# for i in range(n):
#     cnt = 0
#     for j in range(n):
#         if people[i] == cnt and answer[j] == 0:
#             answer[j] = i + 1
#             break
#         elif answer[j] == 0:
#             cnt += 1
# print(*answer)

