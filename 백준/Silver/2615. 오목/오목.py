omok = [list(map(int,input().split())) for _ in range(19)]

del_x = [-1,0,1,1]
del_y = [1,1,1,0]

answer = 0

for x in range(19):
    for y in range(19):

        # 바둑판에서 0이 아니면 돌임
        if omok[x][y] != 0:
            
            for k in range(4):
                cnt = 1
                ox = x + del_x[k]
                oy = y + del_y[k]

                while True:
                    if not(-1 < ox < 19 and -1 < oy < 19):
                            break

                    if omok[x][y] != omok[ox][oy]:
                        break

                    cnt += 1
                    ox = ox + del_x[k]
                    oy = oy + del_y[k]

                    
                if cnt == 5:
                    prev_x = x - del_x[k]
                    prev_y = y - del_y[k]
                    if not (-1 < prev_x < 19 and -1 < prev_y < 19) or omok[x][y] != omok[prev_x][prev_y]:
                        print(omok[x][y])
                        print(x + 1, y + 1)
                        answer = omok[x][y]
if answer == 0:
    print(answer)