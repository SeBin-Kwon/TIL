import Foundation

let n = Int(readLine()!)!
var count = 0
var compare = n

while true {
    count += 1
    let sumNum = compare / 10 + compare % 10
    let newNum = sumNum < 10 ? (compare % 10) * 10 + sumNum : (compare % 10) * 10 + (sumNum % 10)
    if newNum == n {
        print(count)
        break
    }
    compare = newNum
}
