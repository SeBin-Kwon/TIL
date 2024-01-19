a = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):
    answer = 1
    dic = {}
    for cloth in clothes:
        dic[cloth[1]] = dic.get(cloth[1], 0) + 1

    for key in dic:
        answer *= dic[key] + 1
        
    return answer - 1

print(solution(a))


