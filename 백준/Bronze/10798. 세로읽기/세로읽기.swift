import Foundation

var board: [[String]] = .init(repeating: .init(repeating: "", count: 15), count: 5)
var answer = ""

for i in 0..<5 {
    let input = readLine()!.map { String($0) }
    for j in 0..<input.count {
        board[i][j] = input[j]
    }
}

for i in 0..<15 {
    for j in 0..<5 {
        if board[j][i] != "" {
            answer += board[j][i]
        }
    }
}

print(answer)