id_list = ["muzi", "frodo", "apeach", "neo"]
report =["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
answer = []
k = 2

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

for q in range(len(l)):
    if dic[l[q][1]] >= k:
        mail[id_list.index(l[q][0])] += 1

print(mail)