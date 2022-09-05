n = int(input())
dic = {}
for _ in range(n):
    name, log = input().split()
    dic[name] = log

result = []
for k,v in dic.items():
    if v == 'enter':
        result.append(k)
print(*sorted(result, reverse=True),sep='\n')