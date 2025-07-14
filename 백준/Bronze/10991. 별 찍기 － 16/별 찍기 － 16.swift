import Foundation

let n = Int(readLine()!)!
var answer = ""
var space = n - 1
for i in 1...n {
    if i == 1 {
        answer += String(repeating: " ", count: space) + "*\n"
        space -= 1
    } else {
        answer += String(repeating: " ", count: space)
        answer += String(repeating: "* ", count: i - 1)
        answer += "*\n"
        space -= 1
    }
}
print(answer)