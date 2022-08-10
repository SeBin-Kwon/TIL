T = int(input())
grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

for t in range(1, T+1):
    n, k = map(int,input().split())
    total = []

    for stu in range(n):
        mid, final, ass = map(int,input().split())
        total.append((mid*35/100)+(final*45/100)+(ass*20/100))

        s_total = sorted(total,reverse=True)

    pct = n//10
    k_index = s_total.index(total[k-1])

    print(f'#{t}',grade[k_index//pct])