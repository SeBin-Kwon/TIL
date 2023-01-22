import sys
sys.stdin = open('2527.txt', 'r')
input = sys.stdin.readline

for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    if p1 < x2 or p2 < x1 or y1 > q2 or y2 > q1:
        print('d')
        continue
    elif x1 == p2 or x2 == p1:
        if q1 == y2 or q2 == y1:
            print('c')
            continue
        else:
            print('b')
            continue
    elif q1 == y2 or q2 == y1:
        print('b')
        continue
    else:
        print('a')
        continue

# for t in range(4):
#     x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())
#     if x2 > p1 or x1 > p2 or y2 > q1 or y1 > q2:
#         print('d')
#     elif (x1 == p2 and y1 == q2) or (p1 == x2 and q1 == y2) or (p2 == x1 and q1 == y2) or (x1 == p2 and y2 == q1):
#         print('c')
        
#     elif x1 == p2 or y1 == q2 or p1 == x2 or q1 == y2:
#         print('b')

#     else:
#         print('a')

# for t in range(4):
#     x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())
#     if x2 > p1 or x1 > p2 or y2 > q1 or y1 > q2:
#         print('d')

#     elif x1 == p2 or p1 == x2:
#         if (x1 == p2 and y1 == q2) or (x2 == p1 and y2 == q1):
#             print('c')
#         else:
#             print('b')
#     elif q1 == y2 or q2 == y1:
#         if (p2 == x1 and q1 == y2) or (p1 == x2 and q2 == y1):
#             print('c')
#         else:
#             print('b')
#     else:
#         print('a')