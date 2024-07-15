func solution(_ n:Int, _ m:Int) -> [Int] {
    var answer = [Int]()
    var max = min(n, m)
    
    for i in 1...max {
        if n % i == 0 && m % i == 0 {
            max = i
        }
    }
    answer.append(max)
    answer.append(n*m/max)
    return answer
}