func solution(_ s:String) -> String {
    let answer = String(s.sorted(by: > ))
    return answer
}