import Foundation

var arr = [Int]()
for _ in 0..<9 {
    arr.append(Int(readLine()!)!)
}
var notSeven = (0, 0)
arr.sort()
let sumNum = arr.reduce(0, +)
for i in 0..<9-1 {
    for j in i+1..<9 {
        if sumNum - arr[i] - arr[j] == 100 {
            notSeven = (i, j)
        }
    }
}

for i in 0..<9 {
    if i == notSeven.0 || i == notSeven.1 { continue }
    print(arr[i])
}