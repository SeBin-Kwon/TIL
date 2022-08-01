n = int(input())

cards = []
discard = []

for i in range(1,n+1):
    cards.append(i)

while len(cards) > 1:
    discard.append(cards.pop(0))
    cards.append(cards.pop(0))
discard.append(cards[0])
        
print(*discard)