import Foundation

let n = Int(readLine()!)!
let input = readLine()!.split(separator: " ").map { Int($0)! }
var dp = Array(repeating: -1, count: n + 1)

for i in 0..<n {
    let _ = recursive(idx: i)
}

print(dp.max()!)

func recursive(idx: Int) -> Int {
    if idx == n { return 0 }
    if dp[idx] != -1 { return dp[idx] }
    if idx == n - 1 {
        dp[idx] = input[idx]
        return dp[idx]
    }

    dp[idx] = input[idx]
    for i in idx + 1..<n {
        if input[idx] < input[i] {
            dp[idx] = max(dp[idx], input[idx] + recursive(idx: i))
        }
    }

    return dp[idx]
}