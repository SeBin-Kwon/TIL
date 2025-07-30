import Foundation

let n = Int(readLine()!)!
var arr = [(Int, Int)]()
var answer = Int.max

for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    arr.append((input[0], input[1]))
}

func recursive(_ idx: Int, _ s: Int, _ b: Int, _ used: Int) {
    if idx == n {
        if used == 0 { return }
        answer = min(answer, abs(s - b))
        return
    }

    recursive(idx + 1, arr[idx].0 * s, arr[idx].1 + b, used + 1)
    recursive(idx + 1, s, b, used)
}

recursive(0, 1, 0, 0)
print(answer)