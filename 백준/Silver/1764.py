import sys
sys.stdin = open('1764.txt', 'r')

import sys
input = sys.stdin.readline

dict = {}
result = []
n, m = map(int,input().split())

for i in range(n+m):
    name = input().strip('\n')
    if name not in dict:
        dict[name] = 1
    else:
        dict[name] += 1

for k in dict.keys():
    if dict[k] > 1:
        result.append(k)
print(len(result),*sorted(result),sep='\n')
