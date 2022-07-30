n = int(input())
dict = {}
for i in range(n):
    name = input().split()
    dict[name[0]] = name[1]

l = []

for key in dict:
    if dict[key] == 'enter':
        l.append(key)
l.sort(reverse=True)
print('\n'.join(l))