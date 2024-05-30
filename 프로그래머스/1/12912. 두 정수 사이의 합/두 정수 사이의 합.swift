func solution(_ a:Int, _ b:Int) -> Int64 {
    let range = a<b ? a...b : b...a
    let answer = range.reduce(0,+)
    return Int64(answer)
}