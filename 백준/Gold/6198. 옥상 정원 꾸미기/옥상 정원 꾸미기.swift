import Foundation

let n = Int(readLine()!)!
var height = [Int]()
var stack = [Int]()
var answer = 0

for _ in 0..<n {
    let h = Int(readLine()!)!
    height.append(h)
}

for i in 0..<n {
    while !stack.isEmpty && height[stack.last!] <= height[i] {
        stack.removeLast()
    }
    answer += stack.count
    stack.append(i)
}
print(answer)