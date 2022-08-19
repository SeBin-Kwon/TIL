T = int(input())
result = []
for tc in range(1, T+1):
    n = list(input()[::-1])
    for i in range(len(n)):
        if n[i] == 'b':
            n[i] = 'd'
        elif n[i] == 'd':
            n[i] = 'b'
        elif n[i] == 'p':
            n[i] = 'q'
        elif n[i] == 'q':
            n[i] = 'p'

    print(f'#{tc} {"".join(n)}')
