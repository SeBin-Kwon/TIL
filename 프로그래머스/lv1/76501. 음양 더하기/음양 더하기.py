def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            continue
        elif signs[i] == False:
            absolutes[i] = -absolutes[i]
            answer = sum(absolutes)
    return answer