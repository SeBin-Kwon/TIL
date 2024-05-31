func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
    var sortedArr = arr
    var answer = [Int]()
    sortedArr.sort()
    for i in sortedArr {
        if i % divisor == 0 {
            answer.append(i)
        }
    }
    return answer.count == 0 ? [-1] : answer
}