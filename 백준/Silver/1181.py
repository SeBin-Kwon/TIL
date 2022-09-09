import sys
sys.stdin = open('1181.txt', 'r')
input = sys.stdin.readline

n = int(input())
result = []
words = []

for i in range(n):
    s = input().strip('\n')
    words.append(s)
s_words = set(words)
result = sorted(sorted(s_words), key=len)

print(*result,sep='\n')





