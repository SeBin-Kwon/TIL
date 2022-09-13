from collections import deque

n = int(input())

card = deque([])
for i in range(1,n+1):
    card.append(i)

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())
print(*card)



# N = int(input())
# deque = deque([i for i in range(1, N+1)])

# while(len(deque) >1):
#     deque.popleft()
#     move_num = deque.popleft()
#     deque.append(move_num)
    
# print(deque[0])