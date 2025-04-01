import Foundation

let n = Int(readLine()!)!
let input = readLine()!.split(separator: " ").map { Int($0)! }
var y = 0
var m = 0

for i in 0..<n {
    let money = input[i]
    y += (money / 30) * 10
    if money % 30 >= 0 {
      y += 10
    }
    m += (money / 60) * 15
    if money % 60 >= 0 {
      m += 15
    }
}

if y > m {
    print("M \(m)")
} else if y < m {
    print("Y \(y)")
} else {
    print("Y M \(y)")
}