import sys
input = sys.stdin.readline

m = int(input())
set_ = set()
for i in range(m):
    cmd = input().split()
    if len(cmd) == 1:
        if cmd[0] == 'all':
            set_ = {i for i in range(1,21)}
        else:
            set_ = set()
    else:
        x = int(cmd[1])
        if cmd[0] == 'add':
            set_.add(x)
        elif cmd[0] == 'check':
            if x in set_:
                print(1)
            else:
                print(0)
        elif cmd[0] == 'remove':
            set_.discard(x)
        elif cmd[0] == 'toggle':
            if x in set_:
                set_.discard(x)
            else:
                set_.add(x)