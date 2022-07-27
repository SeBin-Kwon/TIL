word = input()
l = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in l:
    word = word.replace(i,'a')
print(len(word))