import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
var numArr = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0], m = input[1]

numArr.sort()
var arr = Array(repeating: -1, count: m)
var visited = Array(repeating: false, count: n)

permu(0)

func permu(_ k: Int) {
    if k == m {
        for i in 0..<m { print(arr[i], terminator: " ") }
        print()
        return
    }
    var before = 0
    for i in 0..<n {
        if !visited[i] && before != numArr[i] {
            before = numArr[i]
            arr[k] = numArr[i]
            visited[i] = true
            permu(k + 1)
            visited[i] = false
        }
    }
}
