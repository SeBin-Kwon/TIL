func solution(_ seoul:[String]) -> String {
    for (i,name) in seoul.enumerated() {
        if name == "Kim" {
            return "김서방은 \(i)에 있다"
        }
    }
    return ""
}