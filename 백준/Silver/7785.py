import sys
sys.stdin = open('7785.txt','r')

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


# def sol():
#     a=open(0)
#     next(a)
#     now=set()
#     for i,ii in map(str.split,a):
#         if i in now:
#             now.remove(i)
#         else:
#             now.add(i)
#     print('\n'.join(sorted(now,reverse=True)))
# sol()

# import sys
# read = sys.stdin.readline

# d = {}
# for _ in range(int(read())):
#     name, action = read().split()
#     if action == 'enter':
#         d[name] = True
#     elif action == 'leave':
#         if name in d:
#             del d[name]
# print('\n'.join(sorted(d.keys(), reverse=True)))

# import sys
# input = sys.stdin.readline

# d = dict()
# for _ in range(int(input())):
#     n, a = input().split()

#     if a == "enter":
#         d[n] = True
#     else:
#         del d[n]

# print('\n'.join(sorted(d.keys(), reverse=True)))