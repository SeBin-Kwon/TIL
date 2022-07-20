import sys

sys.stdin = open("input.txt", "r")

t = int(input())
x = 0
for test_case in range(1,t+1):
    p,q,r,s,w = map(int,input().split())
    a = w*p
    b = (w-r)*s+q
    if w < r:
        if a < q:
            print(f'#{test_case}', a)
        else:
            print(f'#{test_case}', q)
    elif w > r:
        if b < a:
            print(f'#{test_case}', b)
        else:
            print(f'#{test_case}', a)

        


    # if w*p < q:
    #     print(f'#{test_case}', x)
    # elif w*p < (w-r)*s:
    # #a w*p b q,w-r*s
    #     print(f'#{test_case}', x)
    # else :
    #     print(f'#{test_case}', x)