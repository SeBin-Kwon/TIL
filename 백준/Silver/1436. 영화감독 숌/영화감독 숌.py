n = int(input())
cnt = 0
a = 0
while True:
    a += 1
    if '666' in str(a):
        cnt += 1
    if cnt == n:
        break
print(a)