import sys
input = sys.stdin.readline

s, e, q = input().split()

# 시간을 모두 분으로 바꾸기
s = int(s[:2]) * 60 + int(s[3:])
e = int(e[:2]) * 60 + int(e[3:])
q = int(q[:2]) * 60 + int(q[3:])

cnt = 0
dic = {}

while True:
    try:
        chat = input().split()
        c_m = list(map(int,chat[0].split(':')))[0] * 60 + list(map(int,chat[0].split(':')))[1]
        if (chat[1] not in dic) and (c_m <= s):
            dic[chat[1]] = c_m
        elif (e <= c_m <= q) and (chat[1] in dic):
            dic.pop(chat[1])
            cnt += 1
    except:
        break

print(cnt)