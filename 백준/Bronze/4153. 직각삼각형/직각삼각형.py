while True:
    l = list(map(int,input().split()))
    if sum(l) == 0:
        break
    m = max(l)
    l.remove(max(l))
    if l[0]**2 + l[1]**2 == m**2:
        print('right')
    else:
        print('wrong')