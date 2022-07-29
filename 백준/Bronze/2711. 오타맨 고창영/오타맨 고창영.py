T = int(input())
for tc in range(T):
    p, w = input().split()
    print(w[:int(p)-1]+w[int(p):])