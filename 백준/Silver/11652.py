import sys
sys.stdin = open('11652.txt', 'r')

n = int(input())
dic = {}
for _ in range(n):
    m = int(input())
    if m not in dic:
        dic[m] = 1
    else:
        dic[m] += 1

result = sorted(dic.items(), key = lambda x : (-x[1],x[0]))
print(result[0][0])
