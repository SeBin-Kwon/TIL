import sys
sys.stdin = open('1076.txt','r')
color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

num = []
for _ in range(3):
    r = input()
    num.append(color.index(r))
print((num[0]*10+num[1])*(10**num[2]))