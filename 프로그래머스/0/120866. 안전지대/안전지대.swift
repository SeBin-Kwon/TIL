import Foundation

func solution(_ board:[[Int]]) -> Int {
    var safeBoard = Array(repeating: Array(repeating: 0, count: board.count), count: board.count)
    
    let dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    let dx = [0, 1, 1, 1, 0, -1, -1, -1]
    
    for y in 0..<board.count {
        for x in 0..<board.count {
            if board[y][x] == 1 {
                safeBoard[y][x] = 1
                
                for dir in 0..<8 {
                    let ny = y + dy[dir]
                    let nx = x + dx[dir]
                    
                    if ny < 0 || ny >= board.count || nx < 0 || nx >= board.count { continue }
                    
                    safeBoard[ny][nx] = 1
                }
            }
        }
    }
    
    var answer = 0
    for y in 0..<board.count {
        for x in 0..<board.count {
            if safeBoard[y][x] == 0 {
                answer += 1
            }
        }
    }
    
    return answer
}