func solution(_ x:Int, _ n:Int) -> [Int64] {
    var answer = [Int64]()
    answer.append(Int64(x))
    var temp = x
    for i in 0..<n-1 {
        temp += x
        answer.append(Int64(temp))
    }
    return answer
}