import sys
sys.stdin = open('13414.txt', 'r')
input = sys.stdin.readline

K, L = map(int,input().split())
dic = {}
for i in range(L):
    dic[input().strip('\n')] = i
result = sorted(dic.items(), key=lambda x : x[1])
for i in result[:K]:
    print(i[0])

# K, L = map(int, input().split())
# students = [input().rstrip() for _ in range(L)]
# print(list(dict.fromkeys(students[::-1]))[:-K-1:-1])
