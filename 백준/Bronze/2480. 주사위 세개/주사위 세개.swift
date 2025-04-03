import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let (a, b, c) = (input[0], input[1], input[2])

if a == b && b == c {
    print(10_000 + (a * 1_000))
} else if a == b || a == c {
    print(1_000 + a * 100)
} else if b == c {
    print(1_000 + b * 100)
} else {
    print(max(a, b, c) * 100)
}