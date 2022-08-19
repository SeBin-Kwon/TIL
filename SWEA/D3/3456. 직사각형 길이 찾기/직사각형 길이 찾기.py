T = int(input())

for tc in range(1, T+1):
    length = list(map(int,input().split()))
    for i in range(3):
        if length.count(length[i]) == 1:
            print(f'#{tc} {length[i]}')
        elif length.count(length[i]) == 3:
            print(f'#{tc} {length[i]}')
            break