import Foundation

let _ = Int(readLine()!)!
let arr = readLine()!.split(separator: " ").map { Int($0)! }
let x = Int(readLine()!)!
var count = 0

arr.forEach {
    if $0 == x {
        count += 1
    }
}

print(count)