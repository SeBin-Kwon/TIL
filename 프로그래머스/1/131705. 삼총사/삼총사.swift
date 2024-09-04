import Foundation

func solution(_ number:[Int]) -> Int {
    // 3가지 수를 더했을 때 0이 되는 경우의 수 구하기
    var answer = 0
    for i in 0..<number.count-2 {
        for j in i+1..<number.count-1 {
            for k in j+1..<number.count {
                if number[i] + number[j] + number[k] == 0 {
                    answer += 1
                }
            }
        }
    }
    return answer
}