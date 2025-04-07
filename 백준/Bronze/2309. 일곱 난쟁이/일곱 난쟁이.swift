import Foundation

var list = [Int]()
for _ in 0..<9 {
    let num = Int(readLine()!)!
    list.append(num)
}
let remain = list.reduce(0, +) - 100
var a = 0
var b = 0
var flag = false
for i in 0..<9 {
    for j in i+1..<9 {
        if list[i] + list[j] == remain {
            a = i
            b = j
            flag = true
            break
        }
    }
    if flag { break }
}
for num in list.sorted() {
    if num == list[a] || num == list[b] { continue }
    print(num)
}