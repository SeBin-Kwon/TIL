n = int(input())
m = list(map(int,input().split()))
milk = 0

for i in m:
    if i == milk % 3:
        milk += 1
print(milk)
