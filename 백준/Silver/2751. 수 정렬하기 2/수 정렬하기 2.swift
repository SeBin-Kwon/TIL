import Foundation


let n = Int(readLine()!)!
var arr = [Int]()

for _ in 0..<n {
    let input = Int(readLine()!)!
    arr.append(input)
}

arr.sort()

var answer = ""

for ele in arr {
    answer += "\(ele)\n"
}

print(answer)