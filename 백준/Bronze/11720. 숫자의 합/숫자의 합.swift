import Foundation

let n = Int(readLine()!)!
let input = readLine()!.map { Int(String($0))! }
var answer = 0
for i in 0..<n {
    answer += input[i]    
}
print(answer)