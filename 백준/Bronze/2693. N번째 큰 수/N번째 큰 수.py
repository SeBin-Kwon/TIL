t = int(input())
for _ in range(t):
    a = list(map(int,input().split()))
    print(sorted(a, reverse=True)[2])