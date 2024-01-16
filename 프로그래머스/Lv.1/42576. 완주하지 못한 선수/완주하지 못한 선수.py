def solution(participant, completion):
    dic = {}
    for p in participant:
        dic[p] = dic.get(p, 0) + 1
    for c in completion:
        dic[c] -= 1
    
    for k, v in dic.items():
        if v != 0:
            return k