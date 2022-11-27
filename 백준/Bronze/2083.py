import sys
sys.stdin = open('2083.txt','r')

user = []
while True:
    name, age, kg = input().split()
    if name == '#':
        break
    if int(age) > 17 or int(kg) >= 80:
        user.append((name, 'Senior'))
    else:
        user.append((name, 'Junior'))

for i in user:
    print(*i)
