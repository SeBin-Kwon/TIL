import Foundation

let t = Int(readLine()!)!
for _ in 0..<t {
    let _ = Int(readLine()!)!
    var input = readLine()!.split(separator: " ").map { Int($0)! }
    var answer = 0
    input.sort { $0 > $1 }
    for i in 0..<input.count - 1 {
        answer += input[i] - input[i+1]
    }
    print(answer * 2)
}