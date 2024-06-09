func solution(_ n:Int) -> Int {
    guard n > 1 else { return n }
    var answer = 1 + n
    for i in 2..<n {
        if n % i == 0 {
            answer += i
        }
    }
    return answer
}