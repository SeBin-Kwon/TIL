def solution(arr):
    answer = []
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i-1])
        if i == len(arr)-1:
            answer.append(arr[i])
        if arr[i-1] == arr[i]:
            continue            
        
    return answer