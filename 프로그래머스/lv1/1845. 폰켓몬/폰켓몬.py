# n 중 n/2 가져가기
# 번호가 곧 종류 => key
# 밸류는 리스트로 저장?
# 최대한 많은 종류 n/2마리 선택 하는 방법, 종류 번호 개수 return

def solution(nums):
    answer = 0
    takenum = len(nums) // 2
    setnums = len(set(nums))
    if takenum < setnums:
        answer = takenum
    else:
        answer = setnums
    
    return answer