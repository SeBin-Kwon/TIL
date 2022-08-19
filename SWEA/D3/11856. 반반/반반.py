T = int(input())
for t in range(1,T+1):
    s = input()
    flg = True
    for i in s:
        if s.count(i) == 2:
            continue
        else:
            flg = False
            break
    if flg:    
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')