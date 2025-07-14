import Foundation

let n = Int(readLine()!)!
var outSpace = n - 1
var inSpace = 1
var answer = ""

if n == 1 {
    print("*")
} else {
    for i in 1...n {
        if i == n {
            answer += String(repeating: "*", count: n + i - 1)
        } else if i == 1 {
            answer += String(repeating: " ", count: outSpace) + "*\n"
            outSpace -= 1
        } else {
            answer += String(repeating: " ", count: outSpace)
            answer += "*"
            answer += String(repeating: " ", count: inSpace)
            answer += "*\n"
            outSpace -= 1
            inSpace += 2
        }
    }
    print(answer)
}