import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
var numArr = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0], m = input[1]
numArr.sort()
var arr = Array(repeating: -1, count: m)

combi(0, 0)

func combi(_ k: Int, _ s: Int) {
    if k == m {
        for i in 0..<m { print(arr[i], terminator: " ") }
        print()
        return
    }

    for i in s..<n {
        arr[k] = numArr[i]
        combi(k + 1, i + 1)
    }
}