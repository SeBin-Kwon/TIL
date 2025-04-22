import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let (n, k) = (input[0], input[1])
var count = 0
var sum = 0
var money = [Int]()
for _ in 0..<n {
    let num = Int(readLine()!)!
    money.append(num)
}
money.sort(by: >)
for i in 0..<n {
    if money[i] > k { continue }
    while true {
        if sum + money[i] > k { break }
        sum += money[i]
        count += 1
    }
}
print(count)