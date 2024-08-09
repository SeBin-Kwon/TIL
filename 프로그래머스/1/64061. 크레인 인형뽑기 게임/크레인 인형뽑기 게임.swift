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
        if stack.count > 1 {
            guard let first = stack.popLast() else { continue }
            guard let second = stack.popLast() else { continue }
            guard first == second else {
                stack.append(second)
                stack.append(first)
                continue 
            }
            answer += 2
        }
    }
    
    return answer
}