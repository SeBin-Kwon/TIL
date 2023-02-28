import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
# 오름차순 정렬
nums.sort()

def twoPointer():
    # 배열의 양 끝단 인덱스 설정
    left = 0
    right = n - 1
    min_ = sys.maxsize

    while left < right:
        # 현재 지점의 합
        current = nums[left] + nums[right]

        # 만약 현재 지점의 합이 더 0에 가깝다면
        if abs(current) < min_:
            # 갱신하기
            min_ = abs(current)
            min_left = nums[left]
            min_right = nums[right]
        
        # 현재 지점의 합이 음수라면 
        if current < 0:
            # 왼쪽을 오른쪽으로 한 칸 옮겨서 0에 가깝게 만들기
            left += 1
        else:
            right -= 1

    return min_left, min_right

print(*twoPointer())