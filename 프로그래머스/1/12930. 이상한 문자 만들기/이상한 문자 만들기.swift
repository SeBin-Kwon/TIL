func solution(_ s:String) -> String {
    var answer = [String]()
    var index = 0
    for chr in s {
        if index % 2 == 0 {
            answer.append(String(chr.uppercased()))
        } else {
            answer.append(String(chr.lowercased()))
        }
        index += 1
        if chr == " " {
            index = 0
        }
    }
    return answer.joined()
}