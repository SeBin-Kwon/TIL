import sys

input = sys.stdin.readline

n, m = map(int,input().split())
f = True
for i in range(m):
    book_stack = int(input())
    book = list(map(int,input().split()))
    
    if book != sorted(book,reverse=True):
        f = False
        break

print('Yes' if f == True else 'No')