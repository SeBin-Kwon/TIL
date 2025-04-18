import Foundation

let input = readLine()!.map { Int(String($0))! }
var count = Array(repeating: 0, count: 10)

for i in input {
    if i == 6 || i == 9 {
        if count[6] < count[9] {
            count[6] += 1
        } else {
            count[9] += 1
        }
    } else {
        count[i] += 1
    }
}

print(count.max()!)