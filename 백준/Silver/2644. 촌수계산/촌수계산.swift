import Foundation

let n = Int(readLine()!)!
let find = readLine()!.split(separator: " ").map { Int($0)! }
let m = Int(readLine()!)!
var adjList: [[Int]] = Array(repeating: [], count: n + 1)

var visitied = Array(repeating: -1, count: n + 1)
var front = 0
var queue = [Int]()

for _ in 0..<m {
    let edge = readLine()!.split(separator: " ").map { Int($0)! }
    let x = edge[0], y = edge[1]
    adjList[x].append(y)
    adjList[y].append(x)
}

queue.append(find[0])
visitied[find[0]] = 0

while queue.count >= front + 1 {
    let current = queue[front]
    front += 1

    for degree in adjList[current] {
        if visitied[degree] != -1 { continue }
        queue.append(degree)
        visitied[degree] = visitied[current] + 1
    }
}

print(visitied[find[1]])