import Foundation

let n = Int(readLine()!)!
for i in 0..<n {
    let input = readLine()!
    var count = 0
    var answer = ""
    for ele in input {
        if ele == "(" {
            count += 1
        } else if ele == ")" {
            count -= 1
        }

        if count < 0 {
            answer = "NO"
            break
        }
    }
    if !answer.isEmpty {
        print(answer)
    } else {
        answer = count == 0 ? "YES" : "NO"
        print(answer)
    }
}