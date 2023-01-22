import sys
sys.stdin = open('2852.txt', 'r')
input = sys.stdin.readline

# win = {1:0,2:0}
# score = {1:0,2:0}
# flag = 0
# n = int(input())
# for i in range(n):
#     team, time = input().split()
#     s_time = int(time[:2]) * 60 + int(time[3:])
#     score[int(team)] += 1
#     if score[1] > score[2]:
#         flag = 1
#         if win[1] == 0:
#             win[1] = s_time
#     elif score[1] < score[2]:
#         flag = 2
#         if win[2] == 0:
#             win[2] = s_time
#     else:
#         if flag == 1:
#             if win[2] == 0:
#                 win[2] = s_time
#             win[1] = win[2] - win[1]
#             win[2] = 0
#         elif flag == 2:
#             if win[1] == 0:
#                 win[1] = s_time
#             win[2] = win[1] - win[2]
#             win[1] = 0
#         flag = 0

# if flag != 0:
#     win[flag] = 48*60 - win[flag]
# print(f'{str(win[1] // 60).zfill(2)}:{str(win[1] % 60).zfill(2)}')
# print(f'{str(win[2] // 60).zfill(2)}:{str(win[2] % 60).zfill(2)}')

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