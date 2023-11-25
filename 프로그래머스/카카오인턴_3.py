# 승리할 확률이 가장 높은 주사위 조합 찾기
import itertools

dice = [[1,2,3,4,5,6],
        [3,3,3,3,4,4],
        [1,3,3,4,4,4],
        [1,1,4,4,5,5]]

def solution(dice):
    answer = []
    n = len(dice)//2
    win = 0
    print(list(itertools.combinations(dice,n)))
    for combi in itertools.combinations(dice,n):
        print(combi)
        # for i in itertools.product(*combi):
        #     print(i)
    
    return answer

print(solution(dice))

