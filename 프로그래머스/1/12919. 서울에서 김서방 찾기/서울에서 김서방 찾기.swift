func solution(_ seoul:[String]) -> String {
    var answer = ""
    for (i,name) in seoul.enumerated() {
        if name == "Kim" {
            answer = "김서방은 \(i)에 있다"
        }
    }
    return answer
}