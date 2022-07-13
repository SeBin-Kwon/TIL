#1
n = 267
if n % 3 == 0 and n % 2 == 0:
    print('참')
else:
    print('거짓')

#2
# 문자열 word의 길이를 출력하는 코드를 1) while문 2) for문(문자열 그대로) 3) for문(index)으로 각각 작성하시오.

word = 'happy!'
l = 0
for i in word:
    l += 1
print(l)

#3
# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
n = 10
result = 0
a = 0
while a <= n :
    result += a
    a += 1
print(result)

n = 10
result = 0
a = 0
for a in range(n):
    a += 1
    result += a
print(result)

#다른사람
# n=int(input())
# r=0

# for i in range(n+1):
#     r+=i

# while n!=0:
#     r+=n
#     n-=1

# print(r)

#4번 문제 n까지의 곱
n = 5
result = 1
a = 1

while a <= n :
    result *= a
    a += 1
print(result)

for i in range(1,n+1):
    result *= i
print(result)

#5번문제
numbers = [3, 10, 20]
s = 0
c = 0
for i in numbers:
    s += i
    c += 1
r = s/c
print(r)

#6번문제
#주어진 리스트 numbers에서 최댓값을 구하여 출력하시오.
numbers = [0, 20, 100]
a = numbers[0]
for i in numbers:
    if i > a:
        a = i
    else:
        a = a
print(a)

#7번문제
numbers = [0, 20, 100]
a = numbers[0]
for i in numbers:
    if i < a:
        a = i
    else:
        a = a
print(a)

#8번문제
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