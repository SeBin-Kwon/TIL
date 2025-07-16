import Foundation

typealias Score = (String, Int, Int, Int)

let n = Int(readLine()!)!
var arr = [Score]()

for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map { String($0) }
    arr.append((input[0], Int(input[1])!, Int(input[2])!, Int(input[3])!))
}

arr.sort {
    if $0.1 == $1.1 {
        if $0.2 == $1.2 {
            if $0.3 == $1.3 {
                return $0.0 < $1.0
            } else {
                return $0.3 > $1.3
            }
        } else {
            return $0.2 < $1.2
        }
    } else {
        return $0.1 > $1.1
    }
}

for ele in arr {
    print(ele.0)
}