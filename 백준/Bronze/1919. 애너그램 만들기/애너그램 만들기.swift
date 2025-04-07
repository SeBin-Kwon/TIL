import Foundation

let str = readLine()!
let str2 = readLine()!
var answer = 0

var dict = [Character: Int]()

for cha in str {
    dict[cha, default: 0] += 1
}

for cha in str2 {
    dict[cha, default: 0] -= 1
}

answer = dict.values.reduce(0) {
    abs($0) + abs($1)
}

print(answer)