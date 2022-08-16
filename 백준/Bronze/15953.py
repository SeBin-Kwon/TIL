import sys
sys.stdin = open('15953.txt', 'r')

import sys
input = sys.stdin.readline

a_r, b_r = [0], [0]
a_m, b_m = (500,300,200,50,30,10), (512,256,128,64,32)

for i in range(6):
    for j in range(i+1):
        a_r.append(a_m[i])

for i in range(5):
    for j in range(2**i):
        b_r.append(b_m[i])

# for i in range(6):
#     a_r += [a_m[i] for j in range(i+1)]

# for i in range(5):
#     b_r += [b_m[i] for j in range(2**i)]


for _ in range(int(input())):
    a, b = map(int,input().split())
    if a >= len(a_r):
        a = 0
    if b >= len(b_r):
        b = 0
    print((a_r[a]+b_r[b])*10000)
    
