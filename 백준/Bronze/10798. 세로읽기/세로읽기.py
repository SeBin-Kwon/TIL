result = ''
word = []
leng = []

for _ in range(5):
    a = input()
    word.append(a)
    leng.append(len(a))

for i in range(max(leng)):
    for j in range(5):
        if i < leng[j] :
            result += word[j][i]
print(result)