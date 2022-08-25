import sys
sys.stdin = open('1316.txt','r')

n = int(input())
cnt = 0
for _ in range(n):
    word = input()
    l = ''
    for i in word:
        if i not in l:
            l += i
            continue

        if i in l:
            if i == l[-1]:
                l += i
        
    if word == l:
        cnt += 1
print(cnt)