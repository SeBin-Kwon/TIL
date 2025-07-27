import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let (a, b, c, n) = (input[0], input[1], input[2], input[3])
var flag = false

loop: for i in 0...n/a {
    for j in 0...n/b {
        for k in 0...n/c {
            let sumNum = a * i + b * j + c * k
            if sumNum == n {
                flag = true
                break loop
            } else if sumNum > n {
                break
            }
        }
    }
} 

print(flag ? 1 : 0)