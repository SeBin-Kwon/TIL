import sys
sys.stdin = open('1874.txt', 'r')

n = int(input())
flg = True
stack = []
o = []
cnt = 1

for _ in range(n):
    num = int(input())
   
    while cnt <= num:
        stack.append(cnt)
        o.append('+')
        cnt += 1


    if stack[-1] == num:
        stack.pop()
        o.append('-')

    else:
        flg = False
        break
    
if flg == False:
    print('NO')
else:
    print(*o,sep='\n')
