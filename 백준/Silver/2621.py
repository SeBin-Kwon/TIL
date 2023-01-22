import sys
sys.stdin = open('2621.txt', 'r')
input = sys.stdin.readline

card = []
score = 0
color_cnt = {}
num_cnt = [0] * 10
for i in range(5):
    color, num = input().split()
    card.append((color, int(num)))

card.sort(key= lambda x:x[1])

for i in range(5):
    if card[i][0] not in color_cnt:
        color_cnt[card[i][0]] = 1
    else:
        color_cnt[card[i][0]] += 1
    num_cnt[card[i][1]] += 1

# 연속적인지
def continual():
    flag = True
    for i in range(1,5):
        if card[i-1][1] + 1 != card[i][1]:
            flag = False
            break
    return flag

# 1
if len(color_cnt) == 1 and continual():
    score = card[-1][1] + 900
# 2
elif 4 in num_cnt:
    score = num_cnt.index(4) + 800
# 3
elif 3 in num_cnt and 2 in num_cnt:
    score = num_cnt.index(3)*10 + num_cnt.index(2) + 700
# 4
elif len(color_cnt) == 1:
    score = card[-1][1] + 600
# 5
elif continual():
    score = card[-1][1] + 500
# 6
elif 3 in num_cnt:
    score = num_cnt.index(3) + 400
# 7
elif 2 in num_cnt:
    if num_cnt.count(2) == 2:
        a = num_cnt.index(2)
        num_cnt[a] = 0
        b = num_cnt.index(2)
        score = max(a,b)*10 + min(a,b) + 300
    # 8
    else:
        score = num_cnt.index(2) + 200
# 9
else:
    score = card[-1][1] + 100

print(score)
