import Foundation

let n = Int(readLine()!)!
var candies = [[Character]]()
for _ in 0..<n {
    candies.append(Array(readLine()!))
}
var maxCnt = 1

for i in 0..<n {
    for j in 0..<n {
        if j < n-1 && candies[i][j] != candies[i][j+1] {
            candies[i].swapAt(j, j+1)
            countCandy()
            candies[i].swapAt(j+1, j)
        } 
        if i < n-1 && candies[i][j] != candies[i+1][j] {
            let temp = candies[i][j]
            candies[i][j] = candies[i+1][j]
            candies[i+1][j] = temp

            countCandy()

            candies[i+1][j] = candies[i][j]
            candies[i][j] = temp
        } 
    }
}

print(maxCnt)

func countCandy() {
    for r in 0..<n {
        var cnt = 1
        for c in 1..<n {
            if candies[r][c] == candies[r][c-1] {
                cnt += 1
            } else {
                cnt = 1
            }
            maxCnt = max(maxCnt, cnt)
        }
    }
    for r in 0..<n {
        var cnt = 1
        for c in 1..<n {
            if candies[c][r] == candies[c-1][r] {
                cnt += 1
            } else {
                cnt = 1
            }
            maxCnt = max(maxCnt, cnt)
        }
    }
}