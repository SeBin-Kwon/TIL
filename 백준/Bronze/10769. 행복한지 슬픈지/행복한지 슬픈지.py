n = input()

happy = n.count(':-)')
sad = n.count(':-(')

if happy == 0 and sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
else:
    print('unsure')