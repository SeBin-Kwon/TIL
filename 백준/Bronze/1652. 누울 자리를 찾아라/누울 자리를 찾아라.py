n = int(input())
w_room = [list(input()) for _ in range(n)]
h_room = [[0] * n for _ in range(n)]
w_cnt = 0
h_cnt = 0

for i in range(n):  
    w_space = 0
    h_space = 0
    for j in range(n):
        h_room[i][j] = w_room[j][i]
        if w_room[i][j] == '.':
            w_space += 1
        else:
            w_space = 0

        if w_space == 2:
            w_cnt += 1

        if h_room[i][j] == '.':
            h_space += 1
        else:
            h_space = 0

        if h_space == 2:
            h_cnt += 1

print(w_cnt, h_cnt)