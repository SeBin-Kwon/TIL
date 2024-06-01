func solution(_ s:String) -> String {
    let answer = String(Array(s).sorted(by: > ))
    return answer
}