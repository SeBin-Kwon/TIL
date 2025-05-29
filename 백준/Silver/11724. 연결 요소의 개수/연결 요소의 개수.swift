import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0], m = input[1]
var adjList: [[Int]] = .init(repeating: [], count: n + 1)

for _ in 0..<m {
    let edge = readLine()!.split(separator: " ").map { Int($0)! }
    adjList[edge[0]].append(edge[1])
    adjList[edge[1]].append(edge[0])
}

var visited: [Bool] = .init(repeating: false, count: n + 1)
var count = 0
var queue = [Int]()
var front = 0
for i in 1...n {
    if visited[i] { continue }
    queue.append(i)
    visited[i] = true
    count += 1
    while queue.count >= front + 1 {
        let current = queue[front]
        front += 1

        for degree in adjList[current] {
            if visited[degree] { continue }
            visited[degree] = true
            queue.append(degree)
        }
    }
}
print(count)