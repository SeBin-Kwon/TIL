import Foundation

let n = Int(readLine()!)!
var space = n - 1
for i in 1...n {
    print(String(repeating: " ", count: space) + String(repeating: "*", count: i))
    space -= 1
}