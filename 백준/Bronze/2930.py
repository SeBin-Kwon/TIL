import sys
sys.stdin = open('2930.txt','r')

r = int(input()) # 라운드
s = input() # 상근이
n = int(input()) # 친구 n명
f = [] # 친구들
for _ in range(n):
    f.append(input())

score = 0 # 점수
max_score = 0 # 최대 점수
srp = {'S' : 0, 'R' : 1, 'P' : 2} # 가위바위보를 숫자로 나타냄

#todo (상근이 - 친구) % 3을 한 결과에 따라 승패가 나뉨
# {'S' : 0, 'R' : 1, 'P' : 2}는 승 == 1, 패 == 2
#? 만약 {'S' : 0, 'P' : 1, 'R' : 2} 했으면 승 == 2, 패 == 1

# 라운드 만큼 반복
for i in range(r):

    # 라운드 마다 상근이가 낼 케이스들 초기화
    srp_case = {'S' : 0, 'R' : 0, 'P' : 0}

    # 친구 n명 반복
    for j in range(n):

        # 이긴 경우 2점 추가
        if (s[i] == 'S' and f[j][i] == 'P') or (s[i] == 'P' and f[j][i] == 'R') or (s[i] == 'R' and f[j][i] == 'S'):
            score += 2
        # 비긴 경우 1점 추가
        elif s[i] == f[j][i]:
            score += 1
        
        #! 진 경우 만들어서 continue 해버리면 밑에 for문 생략됨..
        
        # 가위바위보 반복
        for k in srp:

            # 딕셔너리로 접근해서 이긴 경우 2점 추가
            if (srp[k]-srp[f[j][i]]) % 3 == 1:
                srp_case[k] += 2

            # 비긴 경우 1점 추가
            elif (srp[k]-srp[f[j][i]]) % 3 == 0:
                srp_case[k] += 1

    # 친구 n명 반복 다 끝나고 딕셔너리 밸류 최대값을 저장함
    max_score += max(srp_case.values())

print(score, max_score, sep='\n')
    