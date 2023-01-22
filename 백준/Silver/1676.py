n = int(input())
result = 1
for i in range(1,n+1):
    result *= i
cnt = 0
answer = str(result)[::-1]
for j in answer:
    if j == '0':
        cnt += 1
    else:
        break
print(cnt)