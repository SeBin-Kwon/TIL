import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    n = int(input())
    wear = {}
    for i in range(n):
        name, type_ = input().split()
        if type_ in wear:
            wear[type_].append(name)
        else:
            wear[type_] = [name]
    cnt = 1
    for j in wear.values():
        cnt *= len(j) + 1
    print(cnt - 1)