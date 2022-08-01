import sys
sys.stdin = open('1302.txt', 'r')

n = int(input())
dict = {}
result = []

for i in range(n):
    book = input()
    if book not in dict:
        dict[book] = 1
    elif book in dict:
        dict[book] += 1
for k in dict:
    if dict[k] == max(dict.values()):
        result.append(k)
print(sorted(result)[0])

# N = int(input())
# sells = dict()

# for _ in range(N) :
#     book = input()
#     if book in sells :
#         sells[book] += 1
#     else :
#         sells[book] = 1

# sells = sorted(sells.items())
# print(sorted(sells, key=lambda x: x[1], reverse=True)[0][0])
