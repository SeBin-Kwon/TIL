nums = [3,3,3,2,2,2]

def solution(nums):
    answer = 0
    takenum = len(nums) // 2
    setnums = len(set(nums))
    if takenum < setnums:
        answer = takenum
    else:
        answer = setnums
    
    return answer

print(solution(nums))
