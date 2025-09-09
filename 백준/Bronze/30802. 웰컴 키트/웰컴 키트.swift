import Foundation

let n = Int(readLine()!)!
let sizeCount = readLine()!.split(separator: " ").map { Int($0)! }
let input = readLine()!.split(separator: " ").map { Int($0)! }
let (t, p) = (input[0], input[1])
var tCount = 0

for size in sizeCount {
    tCount += (size + t - 1) / t
}

print(tCount)
print("\(n / p) \(n % p)")