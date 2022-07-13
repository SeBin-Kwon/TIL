#두번째로 큰 수
numbers = [-20, -100, -40]
# 비교했을 때 f보다 크면 그 수를 f에 저장, 또 다른 큰 수를 만나면 또 저장, 원래 갖고 있던 값은 s에 버림
f = float("-inf")
s = float("-inf")
for i in numbers:
    if f < i:
        s = f
        f = i
    elif s < i < f:
        s = i
    elif s <= i and s < f:
        s = i
print(s,f)

# numbers = [-20, -100, -40]
# max_number = float("-inf")
# second_number = float("-inf")

# # 1. 전체 숫자를 반복
# for n in numbers:
#     # 만약에, n이 최대보다 크다면
#     if max_number < n:
#         # 최대값이었던 것이 두번째로 큰 수
#         second_number = max_number
#         max_number = n
#     # elif second_number < n < max_number:
#     elif second_number < n and n < max_number:
#         second_number = n
# print(second_number)