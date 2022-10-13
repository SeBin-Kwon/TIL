T = int(input())
for t in range(T):
    word = input()
    len_ = len(word)
    print(word[0],word[len_-1], sep='')