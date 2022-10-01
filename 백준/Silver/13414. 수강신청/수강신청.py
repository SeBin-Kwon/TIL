import sys
input = sys.stdin.readline

K, L = map(int,input().split())
dic = {}
for i in range(L):
    dic[input().strip()] = i
result = sorted(dic.items(), key=lambda x : x[1])
for i in result[:K]:
    print(i[0])