import sys
sys.stdin = open('1157.txt','r')

word = input().upper()
set_word = list(set(word))

cnt = []
for i in set_word:
    cnt.append(word.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')

else:
    print(set_word[cnt.index(max(cnt))])
