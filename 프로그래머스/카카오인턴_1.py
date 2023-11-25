friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

def solution(friends, gifts):
    dic = {}
    next_dic = {}
    check = []
    for i in friends:
        next_dic[i] = [0, 0]
        dic[i] = {j: [0,0] for j in friends}
    for j in gifts:
        j = j.split(" ")
        dic[j[0]][j[1]][0] += 1
        dic[j[1]][j[0]][1] += 1

    for ik,iv in dic.items():
        for k, v in iv.items():
            if ik == k: continue
            if v[0] > v[1]:
                next_dic[ik][0] += 1
            elif v[0] == v[1]:
                if (k, ik) not in check:
                    check.append((ik, k))
            next_dic[ik][1] += v[0] - v[1] 

    for a, b in check:
        if next_dic[a][1] > next_dic[b][1]:
            next_dic[a][0] += 1
        elif next_dic[a][1] < next_dic[b][1]:
            next_dic[b][0] += 1

    answer = max(next_dic.values())[0]
    return answer

print(solution(friends, gifts))