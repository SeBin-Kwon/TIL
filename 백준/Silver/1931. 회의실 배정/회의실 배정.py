import sys

input = sys.stdin.readline

n = int(input())
meetings = []
for _ in range(n):
    s,e = map(int,input().split())
    meetings.append((s,e))
meetings.sort(key= lambda x : (x[1], x[0]))

cnt = 1
end_ = meetings[0][1]

for i in range(1,n):
    if meetings[i][0] >= end_:
        cnt += 1
        end_ = meetings[i][1]

print(cnt)