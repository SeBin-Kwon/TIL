import sys
sys.stdin = open('1107.txt', 'r')
input = sys.stdin.readline

# 0~9 10개, +1, -1, 채널은 무한대
# 이동하려는 채널 n
# 버튼 하나 고장났을 때, n채널로 이동하기 위한 최소 버튼 횟수 구하기
# 지금 보고 있는 채널은 100번, n == 100이면 무조건 답은 0
# 고장난 버튼을 제외한 가장 근접한 수 입력(절대값)
# +1씩 해줌
# 숫자 입력 횟수 + 1횟수
#* 갈 수 있는 모든 채널을 다 돌아서
#* 그 채널의 숫자를 누를 수 있는지 없는지 판단, 못누르면 패스
#* 다 누를 수 있으면
#* 채널 100번에서 +1씩 가는게 작은지, 해당 채널에서 +1씩 + 채널누르는 횟수가 더 작은지


# n = input().rstrip()
# m = int(input())
# broken = list(map(int, input().split()))
# cnt, plus, minus = 0, 0, 0
# almost_n = ''

# if n == '100':
#     print(0)
# else:
#     button = []
#     for i in range(10):
#         if i not in broken:
#             button.append(i)
#     # [0, 1, 2, 3, 4, 5, 9]
#     for num in n:
#         if int(num) in button:
#             almost_n += num
#         else:
#             temp = 1e9
#             min_idx = 0
#             for i in range(len(button)):
#                 if abs(int(num) - button[i]) < temp:
#                     temp = abs(int(num) - button[i])
#                     min_idx = i
#             almost_n += str(button[min_idx])
#         cnt += 1
#     print(abs(int(n) - int(almost_n)) + cnt)
            
n = int(input()) 
m = int(input())
if m: 
    broken = set(input().split())
else:
    broken = set()
    
min_count = abs(100 - n)

for nums in range(1000001): 
    for i in str(nums):
        if i in broken:
            break
    else:
        min_count = min(min_count, len(str(nums)) + abs(nums - n))

print(min_count)