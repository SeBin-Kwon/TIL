def solution(id_list, report, k):
    l = []
    dic = {}
    mail = [0] * len(id_list)

    # 중복 제거
    report = list(set(report))

    for i in report:
        r1, r2 = i.split()
        l.append((r1,r2))


    # 신고 당한 사람
    for j in range(len(l)):
        if l[j][1] not in dic:
            dic[l[j][1]] = 1
        else:
            dic[l[j][1]] += 1  
    # {'frodo': 2, 'neo': 2, 'muzi': 1}

    # for a in range(len(cnt)):
    #     if cnt[a] >= k:
    #         stop.append(id_list[a])

    # [('muzi', 'frodo'), ('apeach', 'frodo'), ('frodo', 'neo'), ('muzi', 'neo'), ('apeach', 'muzi')]
    for q in range(len(l)):
        if dic[l[q][1]] >= k:
            mail[id_list.index(l[q][0])] += 1

    return mail