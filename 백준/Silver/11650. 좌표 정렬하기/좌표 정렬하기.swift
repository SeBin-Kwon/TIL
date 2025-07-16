import Foundation

typealias Pos = (Int, Int)

let n = Int(readLine()!)!
var arr = [Pos]()

for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    arr.append((input[0], input[1]))
}

arr.sort {
    if $0.0 == $1.0 {
        return $0.1 < $1.1
    } else {
        return $0.0 < $1.0
    }
}

var answer = ""

for ele in arr {
    answer += "\(ele.0) \(ele.1)\n"
}

print(answer)