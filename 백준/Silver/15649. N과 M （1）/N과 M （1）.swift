import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0], m = input[1]
var visited = Array(repeating: false, count: n)
var arr = Array(repeating: -1, count: m)

permu(0)
func permu(_ k: Int) {
    if k == m {
        for i in 0..<m { print("\(arr[i])", terminator: " ") }
        print()
        return
    }
    
    for i in 0..<n {
        if !visited[i] {
            arr[k] = i + 1
            visited[i] = true
            permu(k + 1)
            visited[i] = false
        }
    }
}