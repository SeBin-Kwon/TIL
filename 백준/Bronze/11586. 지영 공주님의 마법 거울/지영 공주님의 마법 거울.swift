import Foundation

let n = Int(readLine()!)!
var mirror = [[String]]()
var answer = [[String]]()
for _ in 0..<n {
    let input = readLine()!.map { String($0) }
    mirror.append(input)
}
let state = Int(readLine()!)!

switch state {
case 1:
    for i in 0..<n {
        print(mirror[i].joined())
    }
case 2:
    for i in 0..<n {
        let reversedMirror = Array(mirror[i].reversed())
        print(reversedMirror.joined())
    }
case 3:
    for i in stride(from: n-1, through: 0, by: -1) {
        answer.append(mirror[i])
    }
    for i in 0..<n {
        print(answer[i].joined())
    }
default:
    for i in 0..<n {
        print(mirror[i].joined())
    }
}