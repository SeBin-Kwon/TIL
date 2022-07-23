n = int(input())
m = n
i = 0
while True:
    m = m%10*10+(m//10+m%10)%10
    i += 1
    if n == m:
        break
print(i)
       