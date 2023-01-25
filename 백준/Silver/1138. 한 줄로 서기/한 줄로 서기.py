import sys
input = sys.stdin.readline

n = int(input())
people = list(map(int,input().split()))[::-1]
answer = []
for i in people:
    answer.insert(i,n)
    n -= 1
print(*answer)