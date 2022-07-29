import sys
sys.stdin = open('10816.txt', 'r')

n = int(input())
card = list(map(int,input().split()))
m = int(input())
number = list(map(int,input().split()))

dict = {}

for i in card:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

for j in number:
    result = dict.get(j)
    if result == None:
        print(0, end=' ')
    else:
        print(result, end=' ')

# for i in number:
#     dict[i] = 0
#     for j in card:
#         if i == j:
#             dict[i] += 1
# for v in dict.values():
#     print(v, end=' ')
