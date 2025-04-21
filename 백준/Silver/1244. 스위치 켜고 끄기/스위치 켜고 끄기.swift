import Foundation

let n = Int(readLine()!)!
var switchList = readLine()!.split(separator: " ").map { Int($0)! }
let personCount = Int(readLine()!)!
for _ in 0..<personCount {
    let person = readLine()!.split(separator: " ").map { Int($0)! }
    let (gender, number) = (person[0], person[1])
    if gender == 1 {
        for i in stride(from: number - 1, to: n, by: number) {
            switchList[i] = 1 - switchList[i]
        }
    } else {
        let idx = number - 1
        var left = idx
        var right = idx
        while left - 1 >= 0 && right + 1 < n && switchList[left - 1] == switchList[right + 1] {
            left -= 1
            right += 1
        }
        for i in left...right {
            switchList[i] = 1 - switchList[i]
        }
    }
}
for i in 0..<n {
    print(switchList[i], terminator: " ")
    if (i + 1) % 20 == 0 {
        print()
    }
}