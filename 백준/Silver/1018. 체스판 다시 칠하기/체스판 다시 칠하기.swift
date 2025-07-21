import Foundation 

let size = readLine()!.split(separator: " ").map { Int($0)! }
let n = size[0], m = size[1]
var board = [[Character]]()
for _ in 0..<n {
    board.append(readLine()!.map { $0 })
}
var answer = 64
for i in 0...n-8 {
    for j in 0...m-8 {
        var w = 0, b = 0
        for k in i..<i+8 {
            for l in j..<j+8 {
                if (k + l) % 2 == 0 {
                    if board[k][l] == "B" {
                        w += 1
                    } else {
                        b += 1
                    }
                } else {
                    if board[k][l] == "W" {
                        w += 1
                    } else {
                        b += 1
                    }
                }
            }
        }
        answer = min(answer, w, b)
    }
}
print(answer)