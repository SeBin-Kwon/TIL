import Foundation

let n = Int(readLine()!)!
var arr = [(Int, Int)]()
var answer = 0

for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    arr.append((input[0], input[1]))
}

recursive(day: 0, sum: 0)
print(answer)

func recursive(day: Int, sum: Int) {
    if day >= n {
        answer = max(answer, sum)
        return
    }

    if day + arr[day].0 <= n {
        recursive(day: day + arr[day].0, sum: sum + arr[day].1)
    }

    recursive(day: day + 1, sum: sum)
}