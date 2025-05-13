import Foundation

let n = Int(readLine()!)!
var board = [[String]]()
for _ in 0..<n {
    board.append(readLine()!.map { String($0) })
}

var isHead = false
var heart = Array(repeating: -1, count: 2)
var body = Array(repeating: 0, count: 5)

for i in 0..<n {
    for j in 0..<n {
        guard board[i][j] == "*" else { continue }
        
        if isHead {
            
            if heart[0] == i && heart[1] > j {
                body[0] += 1
            }
            
            if heart[0] == i && heart[1] < j {
                body[1] += 1
            }
            
            if heart[0] < i && heart[1] == j {
                body[2] += 1
            }
            
            if heart[0] < i && heart[1] > j {
                body[3] += 1
            }
            
            if heart[0] < i && heart[1] < j {
                body[4] += 1
            }
            
        } else {
            heart[0] = i + 1
            heart[1] = j
            isHead = true
        }
    }
}

heart[0] += 1
heart[1] += 1

print(heart.map { String($0) }.joined(separator: " "))
print(body.map { String($0) }.joined(separator: " "))