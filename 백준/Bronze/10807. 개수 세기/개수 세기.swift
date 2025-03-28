import Foundation

let _ = Int(readLine()!)!
let arr = readLine()!.split(separator: " ").map { Int($0)! }
let x = Int(readLine()!)!

print(arr.filter { $0 == x }.count)