n = int(input())
row = [0] * n
cnt = 0

def attack(x):
    for i in range(x): 
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return True
    return False
 
def dfs(start):
    global cnt
    if start == n:
        cnt += 1
        return
    else:
        for i in range(n):
            row[start] = i
            if not attack(start):
                dfs(start + 1)
 
dfs(0)
print(cnt)