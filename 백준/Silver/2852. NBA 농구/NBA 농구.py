n = int(input())
sche = []

for _ in range(n):
    team, clock = input().split()
    team= int(team)
    hour = int(clock[:2])
    minute = int(clock[-2:])
    all = hour * 60 + minute
    sche.append((team, all))
sche.append((0, 48*60))

one, two = 0, 0
one_ans, two_ans = 0, 0
for i in range(len(sche)-1):
    if sche[i][0] == 1:
        one += 1
    elif sche[i][0] == 2:
        two += 1
    if one > two:
        one_ans += (sche[i+1][1] - sche[i][1])
    elif one < two:
        two_ans += (sche[i+1][1] - sche[i][1])
print(f'{str(one_ans//60).zfill(2)}:{str(one_ans%60).zfill(2)}')
print(f'{str(two_ans//60).zfill(2)}:{str(two_ans%60).zfill(2)}')