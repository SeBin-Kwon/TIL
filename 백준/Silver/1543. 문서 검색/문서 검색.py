n = input()
m = input()
cnt = 0
r = n.replace(m,'*')
for i in r:
    if i == '*':
        cnt += 1
print(cnt)
