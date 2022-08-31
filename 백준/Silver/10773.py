import sys
sys.stdin = open('10773.txt', 'r')

k = int(input())
stack = []
for i in range(k):
    stack.append(int(input()))
    if stack[-1] == 0:
        stack.pop()
        stack.pop()
print(sum(stack))