import sys
input = sys.stdin.readline

n, m = map(int,input().split())
dic = {}
for i in range(n):
    site, pw = input().split()
    dic[site] = pw

for j in range(m):
    memo = input().strip('\n')
    print(dic[memo])