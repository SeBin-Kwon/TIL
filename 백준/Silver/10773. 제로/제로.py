k = int(input())
stack = []
for i in range(k):
    stack.append(int(input()))
    if stack[-1] == 0:
        stack.pop()
        stack.pop()
if not stack:
    print('0')
else:
    print(sum(stack))