from tkinter import W


n = int(input())

card = []
for i in range(1,n+1):
    card.append(i)

while True:
    card.pop(0)
    card.append(card.pop(0))
    if len(card)
    print(card)

from collections import deque

N = int(input())
deque = deque([i for i in range(1, N+1)])

while(len(deque) >1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
    
print(deque[0])