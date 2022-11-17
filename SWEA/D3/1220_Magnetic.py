import sys
sys.stdin = open('1220_Magnetic.txt','r')
input = sys.stdin.readline

for t in range(1,11):
    m = int(input())
    table = []
    for i in range(m):
        table.append(list(map(int,input().split())))
    cnt = 0
    for i in range(100):
        stack = []
        for j in range(100):
            # 만약 이미 n극이 들어와 있다면
            if 1 in stack:
                # s극일 때 넣음
                if table[j][i] == 2:
                    stack.pop()
                    cnt += 1
            else:
                if table[j][i] == 1:
                    stack.append(table[j][i])

    print(f'#{t} {cnt}')