# i번째 ~ j번째 숫자까지 자르고 정렬했을 때,
# k번째 수 구하기

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for cmd in commands:
        cut_array = array[cmd[0]-1:cmd[1]]
        cut_array.sort()
        answer.append(cut_array[cmd[2]-1])
    return answer


print(solution(array,commands))