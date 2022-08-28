n = int(input())
m = 1
cnt = 1
while n > m:
    m += 6 * cnt
    cnt += 1
print(cnt)