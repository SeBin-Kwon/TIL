result = ''

word = [input() for _ in range(5)]

for i in range(15):
    for j in range(5):
        if i < len(word[j]) :
            result += word[j][i]
print(result)