import Foundation

let n = Int(readLine()!)!
var answer = ""
for i in stride(from: n, through: 2, by: -1) {
    answer += String(repeating: "*", count: i) + "\n"
}
answer += "*"
print(answer)