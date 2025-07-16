import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let (k, l) = (input[0], input[1])
var dic = [String: Int]()
var count = 0
var printCnt = 0

for _ in 0..<l {
    let person = readLine()!
    count += 1
    dic[person] = count
}
let answer = dic.sorted { $0.value < $1.value }
for ele in answer {
    print(ele.key)
    printCnt += 1
    if printCnt == k {
        break
    }
}