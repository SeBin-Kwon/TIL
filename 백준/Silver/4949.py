import sys
sys.stdin = open('4949.txt', 'r')

# while 점 하나 오면 종료

while True:
    n = input()
    if n == '.':
        break
    g = []

    for i in n:
        if i == '(' or i == '[':
            g.append(i)
        elif i == ')':
            if len(g) != 0 and g[-1] == '(':
                g.pop()
            else:
                g.append(i)
                break
        elif i == ']':
            if len(g) != 0 and g[-1] == '[':
                g.pop()
            else:
                g.append(i)
                break

    if len(g) != 0:
        print('no')
    else:
        print('yes')


