import Foundation

let n = Int(readLine()!)!
var answer = ""

for _ in 0..<n {
    let s = Int(readLine()!)!

    var flag = true
    for i in 2...1000000 {
        if s % i == 0 {
            flag = false
            break
        }
    }
    if flag {
        answer += "YES\n"
    } else {
        answer += "NO\n"
    }
}
print(answer)