s = input()
l = []
for i in range(len(s)):
    l.append(s[i])
    if l[-4:] == ['P','P','A','P']:
        l.pop()
        l.pop()
        l.pop()
if l == ['P']:
    print('PPAP')
else:
    print('NP')