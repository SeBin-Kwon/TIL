import Foundation

typealias Person = (Int, String)
var arr = [Person]()

let n = Int(readLine()!)!
for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map { String($0) }
    arr.append((Int(input[0])!, input[1]))
}

arr.sort { $0.0 < $1.0 }

for ele in arr {
    print("\(ele.0) \(ele.1)")
}