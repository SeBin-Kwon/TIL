import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var gameBoard = board
    var stack = [Int]()
    var answer = 0
    
    for move in moves {
        for i in 0..<board.count {
            guard gameBoard[i][move-1] != 0 else { continue }
            stack.append(gameBoard[i][move-1])
            gameBoard[i][move-1] = 0
            break
        }
        if stack.count > 1, stack[stack.count-1] == stack[stack.count-2] {
            stack.popLast()
            stack.popLast()
            answer += 2
        }
    }
    return answer
}