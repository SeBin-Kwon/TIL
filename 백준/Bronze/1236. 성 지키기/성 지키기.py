n, m = map(int,input().split())
castle = [list(input()) for _ in range(n)]

n_cnt = 0
m_cnt = []


for i in range(n):
    if 'X' not in castle[i]:
        n_cnt += 1

for j in range(m):
        col = [castle[i][j] for i in range(n)]
        if 'X' not in col:
            m_cnt.append(castle[i][j])
               
print(max(n_cnt,len(m_cnt)))