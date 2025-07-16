import Foundation

let n = Int(readLine()!)!
var arr = [String]()
for _ in 0..<n {
    arr.append(readLine()!)
}

arr.sort {
    if $0.count == $1.count {
        let sumFirst = $0.reduce(0) { $0 + (Int(String($1)) ?? 0) }
        let sumSecond = $1.reduce(0) { $0 + (Int(String($1)) ?? 0) }
        if sumFirst == sumSecond {
            return $0 < $1
        } else {
            return sumFirst < sumSecond
        }
    } else {
        return $0.count < $1.count
    }
}

for ele in arr {
    print(ele)
}