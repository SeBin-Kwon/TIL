import sys
sys.stdin = open('19583.txt', 'r')
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
        # 채팅 시간도 분으로 바꾸기
        c_m = list(map(int,chat[0].split(':')))[0] * 60 + list(map(int,chat[0].split(':')))[1]
        # 딕셔너리에 없으면서 시작 전에 채팅쳤으면 딕셔너리에 추가
        if (chat[1] not in dic) and (c_m <= s):
            dic[chat[1]] = c_m
        # 딕셔너리에 있으면서 개강총회 끝 ~ 스트리밍 끝나는 시간 사이에 있으면 빼고 카운트
        elif (e <= c_m <= q) and (chat[1] in dic):
            dic.pop(chat[1])
            cnt += 1
    except:
        break

print(cnt)

