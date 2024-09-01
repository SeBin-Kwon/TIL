import Foundation

func solution(_ numbers:[Int]) -> Int {
    var answer = 45
    for num in numbers {
        answer -= num
    }
    return answer
}