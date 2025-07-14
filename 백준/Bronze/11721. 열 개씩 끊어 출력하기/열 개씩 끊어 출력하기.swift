import Foundation

let input = readLine()!.map { String($0) }
var answer = ""
for i in 0..<input.count {
    answer += input[i]
    if i % 10 == 9 {
        answer += "\n"
    }
}
print(answer)