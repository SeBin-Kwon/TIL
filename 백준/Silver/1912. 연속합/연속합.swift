import Foundation

let n = Int(readLine()!)!
let input = readLine()!.split(separator: " ").map { Int($0)! }
var dp = Array(repeating: Int.min, count: n + 1)
var answer = 0
let _ = recursive(0)
print(dp.max()!)

func recursive(_ idx: Int) -> Int {
    if idx == n { return 0 }
    if dp[idx] != Int.min { return dp[idx] }

    dp[idx] = input[idx]
    dp[idx] = max(dp[idx], recursive(idx + 1) + input[idx])

    return dp[idx]
}