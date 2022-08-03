n = int(input())
p = [list(map(int,input().split())) for _ in range(n)]
score = []
p_score = [[0]*3 for l in range(n)]

for j in range(3):
    game = [p[i][j] for i in range(n)]
    for k in range(n):
        if game.count(game[k]) == 1:
            p_score[k][j] = game[k]
for h in p_score:
    print(sum(h))