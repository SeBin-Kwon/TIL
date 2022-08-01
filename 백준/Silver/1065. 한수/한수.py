n = int(input())
han = 0

for num in range(1,n+1):
    if num <= 99:
        han += 1
    elif num > 99:
        nummber = list(map(int,str(num)))
        if nummber[0] - nummber[1] == nummber[1] - nummber[2]:
            han += 1
print(han)