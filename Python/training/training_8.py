#주어진 리스트 numbers에서 두번째로 큰 수를 구하여 출력하시오.

numbers = [10, 100, 30]
num = set(numbers)
f = numbers[0]
s = numbers[1]

for i in num:
    if i > f:
        f = i
        continue
num.remove(f)
for i in num:
    if i > s:
        s = i
        continue
print(s)

# numbers = [0, 20, 100]
# f = numbers[0]
# s = numbers[1]

# if f < s:
#     f, s = s, f

# for x in numbers:
#     if x > f:
#         s = f
#         f = x
#     elif x == f:
#         continue
#     else:
#         if x >= s:
#             s = x
# print(s)