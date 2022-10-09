import sys
sys.stdin = open('2012.txt', 'r')
input = sys.stdin.readline

n = int(input())
grade = []
# 예상 등수 입력 받기
for i in range(n):
    grade.append(int(input()))
# 예상 등수 정렬
grade.sort()

result = 0
# i는 실제 등수, (실제 등수 - 예상 등수)로 불만도를 구한다.
for i in range(n):
    result += abs((i + 1) - grade[i])
print(result)
