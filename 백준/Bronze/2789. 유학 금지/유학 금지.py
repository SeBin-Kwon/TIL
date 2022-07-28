word = input()

for i in word:
    if i in 'CAMBRIDGE':
        word = word.replace(i,'')
print(word)