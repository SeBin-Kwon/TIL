T = 10
for t in range(1, T+1):
    n = int(input())
    g = input()
    dict = {
        '(' : ')',
        '[' : ']',
        '{' : '}',
        '<' : '>'
    }
    l = []
    result = 1

    for i in g:
        if i in dict.keys():
            l.append(i)
        else:
            if i == dict[l[-1]]:
                l.pop()
            else:
                result = 0
                break
    print(f'#{t}', result)