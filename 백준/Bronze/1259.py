from re import T
import sys
sys.stdin = open('1259.txt','r')

while True:
    n = input()
    if n == '0':
        break

    if n == n[::-1]:
        print('yes')
    else:
        print('no')

    
