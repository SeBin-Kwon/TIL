import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
var numArr = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0], s = input[1]
var arr = [Int]()
var answer = 0

for i in 1...n {
    combi(i, 0)
    arr = []
}
print(answer)

func combi(_ k: Int, _ idx: Int) {
    if k == arr.count {
        if arr.reduce(0, +) == s {
            answer += 1
        }
        return
    }
    for i in idx..<n {
        arr.append(numArr[i])
        combi(k, i + 1)
        arr.removeLast()
    }
}