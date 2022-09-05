import sys
sys.stdin = open('1228.txt','r')

for t in range(1,11):
    # 원본 암호문 길이
    n = int(input())
    # 원본 암호문
    code = input().split()
    # 명령어 개수
    m = int(input())
    # 명령어
    cmd = input().split()

    for i in range(len(cmd)):
        if cmd[i] == 'I':
            position = int(cmd[i+1])
            cnt = int(cmd[i+2])
            for k in range(cnt):
                code.insert(position+k,cmd[i+3+k])
    
    print(f'#{t}',*code[:10])