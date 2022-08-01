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