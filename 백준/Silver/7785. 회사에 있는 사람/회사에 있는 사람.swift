import Foundation

let n = Int(readLine()!)!
var dic = [String: Bool]()
for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map { String($0) }
    if input[1] == "enter" {
        dic[input[0]] = true
    } else {
        dic.removeValue(forKey: input[0])
    }
}

var answer = ""
let keys = dic.keys.sorted { $0 > $1 }
for key in keys {
    answer += "\(key)\n"
}
print(answer)