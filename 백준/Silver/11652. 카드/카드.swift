import Foundation

let n = Int(readLine()!)!
var dic = [Int: Int]()
for _ in 0..<n {
    dic[Int(readLine()!)!, default: 0] += 1
}
let answer = dic.sorted {
    if $0.value == $1.value {
        return $0.key < $1.key
    } else {
        return $0.value > $1.value
    }
}
print(answer[0].key)