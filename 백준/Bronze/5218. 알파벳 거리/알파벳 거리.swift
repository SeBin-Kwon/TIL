import Foundation

let t = Int(readLine()!)!
for _ in 0..<t {
    let input = readLine()!.split(separator: " ")
    let (a, b) = (Array(input[0]), Array(input[1]))
    var answer = Array(repeating: 0, count: a.count)
    for i in 0..<a.count {
        let (aValue, bValue) = (a[i].asciiValue!, b[i].asciiValue!)
        if aValue <= bValue {
            answer[i] = Int(bValue) - Int(aValue)
        } else {
            answer[i] = 26 - (Int(aValue) - Int(bValue))
        }
    }
    let answerStr = "Distances: " + answer.map { String($0) }.joined(separator: " ")
    print(answerStr)
}