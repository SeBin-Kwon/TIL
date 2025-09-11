import Foundation

let n = Int(readLine()!)!
var graph = [[Int]](repeating: [], count: n + 1)
var answer = [Int](repeating: 0, count: n + 1)

for _ in 0..<n-1 {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    graph[input[0]].append(input[1])
    graph[input[1]].append(input[0])
}

func dfs(_ node: Int) {
    for next in graph[node] {
        if answer[next] == 0 {
            answer[next] = node
            dfs(next)
        }
    }
}

answer[1] = -1
dfs(1)

for i in 2...n {
    print(answer[i])
}