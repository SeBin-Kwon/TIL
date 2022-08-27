import sys
# sys.stdin = open('2751.txt', 'r')


n = int(input())
m = []
for i in range(n):
    m.append(int(sys.stdin.readline())) 

m.sort()
print(*m,sep='\n')