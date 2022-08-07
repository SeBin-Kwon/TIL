m = int(input())
cups = [1, 2, 3]
for _ in range(m):
    x, y = map(int,input().split())
    xi = cups.index(x)
    yi = cups.index(y)

    cups[xi], cups[yi] = cups[yi], cups[xi]

print(cups[0])
