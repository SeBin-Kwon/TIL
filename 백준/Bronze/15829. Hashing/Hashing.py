import sys
input = sys.stdin.readline

l = int(input())
word = input()
sum_ = 0
for i in range(l):
    sum_ += (ord(word[i])-96)*(31**i)
print(sum_ % 1234567891)