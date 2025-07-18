import Foundation

let n = Int(readLine()!)!
var board = Array(repeating: Array(repeating: 0, count: 100), count: 100)

for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    for i in input[0]..<input[0]+10 {
        for j in input[1]..<input[1]+10 {
            board[i][j] = 1
        }
    }
}

print(board.reduce(0) { $0 + $1.filter { $0 == 1 }.count })