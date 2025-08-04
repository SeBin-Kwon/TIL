import Foundation

let n = Int(readLine()!)!
var answer = 0
for _ in 0..<n {
    var stack = [Character]()
    let input = Array(readLine()!)
    for cha in input {
        if stack.isEmpty {
            stack.append(cha)
            continue
        }

        let last = stack.popLast()!
        
        if last != cha {
            stack.append(last)
            stack.append(cha)
        }

    }
    if stack.isEmpty {
        answer += 1
    }
}
print(answer)