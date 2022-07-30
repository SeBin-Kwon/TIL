a = list(map(int,input().split()))
b = list(map(int,input().split()))

a_score = 0
b_score = 0

for i in range(10): # 라운드 10
    if a[i] > b[i]:
        a_score += 3
    elif a[i] < b[i]:
        b_score += 3
    else:
        a_score += 1
        b_score += 1
    
if a_score > b_score:
    print(a_score,b_score,'\nA')
elif a_score < b_score:
    print(a_score,b_score,'\nB')
if a_score == b_score:
    for j in range(9,-1,-1):
        if a[j] != b[j]:
            if a[j] > b[j]:
                print(a_score,b_score,'\nA')
                break
            elif a[j] < b[j]:
                print(a_score,b_score,'\nB')
                break
    else:
        print(a_score,b_score,'\nD')