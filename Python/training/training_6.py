#주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
numbers = [0, 20, 100]
a = numbers[0]
for i in numbers:
    if i > a:
        a = i
    else:
        a = a
print(a)
