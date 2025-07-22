import Foundation

let n = Int(readLine()!)!
var answer = 0
for a in 1...n {
    for b in 1...n {
        for c in 1...n {
            guard a + b + c == n else { continue }
            guard a % 2 == 0 else { continue }
            guard c >= b + 2 else { continue }
            answer += 1
        }
    }
}
print(answer)