r = int(input())
s = input()
n = int(input())
f = []
for _ in range(n):
    f.append(input())

score = 0
max_score = 0
srp = {'S' : 0, 'R' : 1, 'P' : 2}

for i in range(r):
    srp_case = {'S' : 0, 'R' : 0, 'P' : 0}

    for j in range(n):
        if (s[i] == 'S' and f[j][i] == 'P') or (s[i] == 'P' and f[j][i] == 'R') or (s[i] == 'R' and f[j][i] == 'S'):
            score += 2

        elif s[i] == f[j][i]:
            score += 1
        
        for k in srp:
            if (srp[k]-srp[f[j][i]]) % 3 == 1:
                srp_case[k] += 2
            elif (srp[k]-srp[f[j][i]]) % 3 == 0:
                srp_case[k] += 1

    max_score += max(srp_case.values())

print(score, max_score, sep='\n')