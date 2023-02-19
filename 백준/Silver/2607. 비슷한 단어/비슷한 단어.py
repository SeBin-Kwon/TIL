import sys
input = sys.stdin.readline

n = int(input())
first = list(input().rstrip())
answer = 0

for i in range(n-1):
    compare = first[:]
    word = input().rstrip()
    cnt = 0
    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1
    if cnt < 2 and len(compare) < 2:
        answer += 1
print(answer)