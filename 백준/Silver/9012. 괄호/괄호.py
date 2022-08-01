T = int(input())

for t in range(T):
    f = True
    vps = []
    ps = input()

    for i in ps:
        if i == '(':
            vps.append(i)

        if i == ')':
            if '(' in vps:
                vps.pop()
            else:
                break

    else:
        if len(vps) == 0:
            f = False     

    print('YES' if f == False else 'NO')