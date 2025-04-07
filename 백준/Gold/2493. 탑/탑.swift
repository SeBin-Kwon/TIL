import Foundation

let n = Int(readLine()!)!
let height = readLine()!.split(separator: " ").map { Int($0)! }
var answer = Array(repeating: 0, count: n)

var stack: [(index: Int, height: Int)] = []

for i in 0..<n {
    while !stack.isEmpty && stack.last!.height < height[i] {
        stack.removeLast()
    }
    if !stack.isEmpty {
        answer[i] = stack.last!.index + 1
    }
    stack.append((i, height[i]))
}

print(answer.map { String($0) }.joined(separator: " "))