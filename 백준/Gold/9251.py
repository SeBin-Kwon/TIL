import sys
sys.stdin = open('9251.txt', 'r')
input = sys.stdin.readline

#TODO 두 수열이 주어졌을 대, 모두의 부분 수열이 되는 수열 중 가장 긴 것 개수
#? 순서만 같으면 됨, 띄어있어도 됨

a, b = input().strip(), input().strip()
a_len, b_len = len(a), len(b)
answer = [0] * b_len

for i in range(a_len):
    cnt = 0
    for j in range(b_len):
        if cnt < answer[j]:
            cnt = answer[j]
        elif a[i] == b[j]:
            answer[j] = cnt + 1
print(max(answer))

# 동적 계획법 
# 누적합