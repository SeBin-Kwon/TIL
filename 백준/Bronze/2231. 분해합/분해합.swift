import Foundation

let n = Int(readLine()!)!
var answer = 0
for i in 1...n {
    let numSum = String(i).map { Int(String($0))! }.reduce(0, +)
    if numSum + i == n {
        answer = i
        break
    }
}
print(answer)