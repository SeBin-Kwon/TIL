import sys
input = sys.stdin.readline

s = input().rstrip('\n')
f = input().rstrip('\n')
l = []

for i in s:
    l.append(i)
    if l[-len(f):] == list(f):
        for j in range(len(f)):
            l.pop()

if l:
    print(''.join(l))
else:
    print('FRULA')