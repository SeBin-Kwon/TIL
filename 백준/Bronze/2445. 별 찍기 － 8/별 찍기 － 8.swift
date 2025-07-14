import Foundation

let n = Int(readLine()!)!
var space = n * 2 - 2
var answer = ""
for i in 1...n {
    answer += String(repeating: "*", count: i)
    answer += String(repeating: " ", count: space)
    answer += String(repeating: "*", count: i)
    space -= 2
    answer += "\n"
}
space = 0
for i in stride(from:n-1, through: 1, by: -1) {
    space += 2
    answer += String(repeating: "*", count: i)
    answer += String(repeating: " ", count: space)
    answer += String(repeating: "*", count: i)
    answer += "\n"
}
print(answer)