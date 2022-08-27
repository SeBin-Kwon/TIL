import sys
sys.stdin = open('5356.txt', 'r')

T = int(input())
for t in range(1,T+1):
    word = [input() for _ in range(5)]
    # len_w = [len(word[i]) for i in range(5)]
    result = ''

    for i in range((len(max(word, key=len)))):
        for j in range(5):
            if i < len(word[j]):
                result += word[j][i]
                
    print(f'#{t} {result}')