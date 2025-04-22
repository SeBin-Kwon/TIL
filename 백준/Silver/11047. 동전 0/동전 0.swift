import Foundation
let input = readLine()!.split(separator: " ").map { Int($0)! }
var (n, k) = (input[0], input[1])
var count = 0
var money = [Int]()
for _ in 0..<n {
    let num = Int(readLine()!)!
    money.append(num)
}
for i in stride(from: n-1, through: 0, by: -1) {
    if money[i] > k { continue }
    count += k / money[i]
    k %= money[i]
}
print(count)