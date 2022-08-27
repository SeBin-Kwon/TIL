import sys
sys.stdin = open('2751.txt', 'r')

p=print
n = int(input())
m = []
for i in range(n):
    m.append(int(sys.stdin.readline())) 

m.sort()
p(*m,sep='\n')