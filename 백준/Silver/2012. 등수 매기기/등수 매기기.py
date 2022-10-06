import sys
input = sys.stdin.readline

n = int(input())
grade = []
for i in range(n):
    grade.append(int(input()))

grade.sort()

result = 0

for i in range(n):
    result += abs((i + 1) - grade[i])
print(result)
