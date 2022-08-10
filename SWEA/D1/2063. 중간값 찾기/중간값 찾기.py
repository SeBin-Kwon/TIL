n = int(input())
score = list(map(int,input().split()))
score.sort()
cen = (n - 1) // 2 
print(score[cen])