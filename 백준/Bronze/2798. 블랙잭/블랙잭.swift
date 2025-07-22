import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0], m = input[1]
let cards = readLine()!.split(separator: " ").map { Int($0)! }
var answer = [Int]()
for i in 0..<cards.count-2 {
    for j in i+1..<cards.count-1 {
        for k in j+1..<cards.count {
            let sumNum = cards[i] + cards[j] + cards[k]
            if sumNum <= m {
                answer.append(sumNum)
            }
        }
    }
}
print(Int(answer.max()!))