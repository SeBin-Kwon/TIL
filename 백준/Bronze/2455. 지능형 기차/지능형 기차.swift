import Foundation

var people = 0
var answer = 0
for _ in 0..<4 {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    let getOff = input[0], getOn = input[1]
    people -= getOff
    people += getOn
    answer = max(answer, people)
}
print(answer)