import sys
input = sys.stdin.readline

prevFes,fes = [0],[0]
prevPrize,prize = (500,300,200,50,30,10),(512,256,128,64,32)
for i in range(6):
    prevFes += [prevPrize[i] for _ in range(i+1)]
for i in range(5):
    fes += [prize[i] for _ in range(2**i)]

for _ in range(int(input())):
    a,b = map(int,input().split())
    if a >= len(prevFes):
        a = 0
    if b >= len(fes):
        b = 0
    print((prevFes[a] + fes[b])*10000)