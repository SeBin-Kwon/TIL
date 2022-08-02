import sys
sys.stdin = open('4949.txt', 'r')

# while 점 하나 오면 종료

n = ''
small = []
large = []

while n != '.' :
    n = input()
    for i in n:
        if i == '(':
            small.append(i)
        elif i == ')':
            if len(small) != 0: 
                small.pop()
                print('yes')
            else:
                print('no')
                break



