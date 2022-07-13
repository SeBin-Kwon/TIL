numbers = [0, 20, 100]
a = numbers[0]
for i in numbers:
    if i < a:
        a = i
    else:
        a = a
print(a)