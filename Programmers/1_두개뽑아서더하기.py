# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):                   # 첫번째 숫자부터 마지막까지 순회하는 반복문
        for j in range(i+1,len(numbers)):           # i 다음부터 순회하는 반복문
            answer.append(numbers[i] + numbers[j])  # 리스트에 인덱싱으로 접근 후, 더한 값을 리스트에 추가함
    answer = sorted(list(set(answer)))              # set으로 중복제거, 리스트 변환 후 정렬
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))