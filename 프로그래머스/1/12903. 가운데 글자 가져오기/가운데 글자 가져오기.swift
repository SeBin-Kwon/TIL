func solution(_ s:String) -> String {
    let answer: String
    let sArray = s.map { String($0) }
    if s.count % 2 != 0 {
        answer = sArray[s.count/2]
    } else {
        answer = sArray[s.count/2-1] + sArray[s.count/2]
    }
    return answer
}