import Foundation

let n = Int(readLine()!)!
var arr = [[Character]]()
var question = [(numArr: [Character], stricke: Int, ball: Int)]()
var answer = 0
for i in 1...9 {
    for j in 1...9 {
        if i == j { continue }
        for k in 1...9 {
            if i == k || j == k { continue }
            arr.append(Array(String(i*100 + j*10 + k)))
        }
    }
}

for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    question.append((Array(String(input[0])), input[1], input[2]))
}

for i in 0..<arr.count {
    var cnt = n
    for j in 0..<n {
        var stricke = 0, ball = 0
        for k in 0..<3 {
            if arr[i][k] == question[j].numArr[k] {
                stricke += 1
            } else if arr[i].contains(question[j].numArr[k]) && arr[i][k] != question[j].numArr[k] {
                ball += 1
            }
        }
        if stricke == question[j].stricke && ball == question[j].ball {
            cnt -= 1
        } else {
            break
        }
    }
    if cnt == 0 {
        answer += 1
    }
}

print(answer)