alpabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

result = 0
word = input()
for i in word:
    for j in alpabet:
        if i in j:
            result += alpabet.index(j)+3
print(result)