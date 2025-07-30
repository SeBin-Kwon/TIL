import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0], m = input[1]
var answer = Array(repeating: -1, count: m)

combi(0, 0)

func combi(_ idx: Int, _ before: Int) {
    if idx == m {
        for i in 0..<m { print(answer[i], terminator: " ") }
        print()
        return
    }

    for i in before..<n {
        answer[idx] = i + 1
        combi(idx + 1, i)
    }
}