import Foundation
let n = Int(readLine()!)!
let m = Int(readLine()!)!
var adjList = Array(repeating: [Int](), count: n + 1)
var queue = [Int]()
var front = 0
var visited = Array(repeating: 0, count: n + 1)

for _ in 0..<m {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    adjList[input[0]].append(input[1])
    adjList[input[1]].append(input[0])
}

queue.append(1)
visited[1] = 1

while queue.count >= front + 1 {
    let current = queue[front]
    front += 1

    for degree in adjList[current] {
        if visited[degree] != 0 { continue }
        queue.append(degree)
        visited[degree] = 1
    }
}

print(visited.reduce(0, +) - 1)