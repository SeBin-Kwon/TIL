fbi = []
for i in range(5):
    n = input()
    if 'FBI' in n:
        fbi.append(n)
        print(i+1, end=' ')

if not fbi:
    print('HE GOT AWAY!')