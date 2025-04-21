import Foundation
let n = Int(readLine()!)!
var mines = Array(repeating: Array(repeating: false, count: n), count: n)
var isOpen = Array(repeating: Array(repeating: false, count: n), count: n)
var answer = Array(repeating: Array(repeating: ".", count: n), count: n)
let dx = [-1, -1, -1, 0, 0, 1, 1, 1]
let dy = [-1, 0, 1, -1, 1, -1, 0, 1]
var flag = false

for i in 0..<n*2 {
    let row = Array(readLine()!)
    for j in 0..<row.count {
        if i < n {
            if row[j] == "*" {
                mines[i][j] = true
            }
        } else {
            if row[j] == "x" {
                isOpen[i-n][j] = true
            }
        }
    }
}
for i in 0..<n {
    for j in 0..<n {
        guard isOpen[i][j] else { continue }
        guard !mines[i][j] else {
            flag = true
            continue
        }
        var count = 0
        for k in 0..<8 {
            guard i+dx[k] >= 0, i+dx[k] < n, j+dy[k] >= 0, j+dy[k] < n else { continue }

            if mines[i+dx[k]][j+dy[k]] {
                count += 1
            }
        }
        answer[i][j] = String(count)
    }
}

if flag {
    for i in 0..<n {
        for j in 0..<n {
            if mines[i][j] {
                answer[i][j] = "*"
            }
        }
    }

}

for row in answer {
    print(row.joined())
}