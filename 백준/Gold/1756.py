import sys
sys.stdin = open('1756.txt','r')
input = sys.stdin.readline

d, n = map(int,input().split())
oven = list(map(int,input().split()))
pizza = list(map(int,input().split()))
cnt = 0

for i in range(1,d):
    if oven[i-1] < oven[i]:
        oven[i] = oven[i-1]

for i in range(d-1,-1,-1):
    if pizza[cnt] > oven[i]:
        continue
    elif pizza[cnt] <= oven[i]:
        cnt += 1
    if cnt == n:
        print(i+1)
        break
    
if cnt != n:
    print(0)


# for i in range(n):
#     for j in range(d):
#         if pizza[i] <= oven[j] and not check[j]:
#             continue
#         elif pizza[i] > oven[j] and not check[j]:
#             check[j-1] = 1
#             break
#         elif check[j]:
#             check[j-1] = 1
#             break
# if cnt == n :
#     for k in range(d):
#         if check[k] == 1:
#             print(k+1)
#             break
# else:
#     print(cnt,0)