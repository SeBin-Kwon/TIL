import Foundation

let n = readLine()!.components(separatedBy: [" "]).map { Int($0)! }
let (a, b) = (n[0], n[1])
var star = String(repeating: "*", count: a)
for _ in 0..<b {
    print(star)
}