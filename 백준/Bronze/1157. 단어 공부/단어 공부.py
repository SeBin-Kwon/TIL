word = input().upper()
word_2 = list(set(word))
l = []
for i in range(len(word_2)):
    l.append(word.count(word_2[i]))

if l.count(max(l)) > 1:
    print('?')
    
else:
    print(word_2[l.index(max(l))])