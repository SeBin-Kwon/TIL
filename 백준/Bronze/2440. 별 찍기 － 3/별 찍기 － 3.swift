import Foundation
let n = Int(readLine()!)!
for i in stride(from: n, through: 1, by: -1) {
    print(String(repeating: "*", count: i))
}