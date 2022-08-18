import sys
sys.stdin = open('20291.txt','r')

n = int(input())
dic = {}
for i in range(n):
    f = input().split('.')
    if f[1] not in dic:
        dic[f[1]] = 1
    else:
        dic[f[1]] += 1
s_dic = sorted(dic.items())

for k,v in s_dic:
    print(k,v)