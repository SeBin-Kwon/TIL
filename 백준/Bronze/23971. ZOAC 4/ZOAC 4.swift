import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let (h, w, n, m) = (input[0], input[1], input[2], input[3])

let rows = (h + n) / (n + 1)
let cols = (w + m) / (m + 1)
print(rows * cols)