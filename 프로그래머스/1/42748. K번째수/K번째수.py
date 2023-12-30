def solution(array, commands):
    answer = []
    for cmd in commands:
        cut_array = array[cmd[0]-1:cmd[1]]
        cut_array.sort()
        answer.append(cut_array[cmd[2]-1])
    return answer