func solution(_ n:Int64) -> [Int] {
    let str = String(n)
    var answer = [Int]()
    
    for chr in str.reversed() {
        answer.append(Int(String(chr))!)
    }
    
    return answer
}