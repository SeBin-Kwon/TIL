import sys
n = sys.stdin.read().replace(' ','').replace('\n','')

# 모든 알파벳의 빈도수 체크용 리스트
a = [0] * 26

for i in n:
    a[ord(i)-97] += 1

for j in range(26):
    if a[j] == max(a):
        print(chr(j+97), end='')