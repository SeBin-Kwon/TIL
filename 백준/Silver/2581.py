start = int(input())
end = int(input())
answer = []
for num in range(start,end+1):
    flag = 0
    if num != 1:
        for i in range(2, num):
            if num % i == 0:
                flag += 1
                break
        if flag == 0:
            answer.append(num)
if answer:
    print(sum(answer))
    print(min(answer))
else:
    print(-1)