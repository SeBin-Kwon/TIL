import Foundation

let input = readLine()!.split(separator: " ").map { String($0) }
var peopleSet = Set<String>()
var gameDic = ["Y": 2, "F": 3, "O": 4]
for _ in 0..<Int(input[0])! {
    peopleSet.insert(readLine()!)
}
let gameCnt = gameDic[input[1]]! - 1
print(peopleSet.count / gameCnt)