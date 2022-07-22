# 리스트중 최댓값 찾고 인덱스값 찾기
l = []
for i in range(9):
    n = int(input())
    l.append(n)
print(max(l), l.index(max(l))+1, sep='\n')

# l=[int(input())for i in range(9)]
# print(max(l),l.index(max(l))+1)