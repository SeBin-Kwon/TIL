import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
var notHeard = Set<String>()
var notSeen = Set<String>()

for _ in 0..<input[0] {
    notHeard.insert(readLine()!)
}

for _ in 0..<input[1] {
    notSeen.insert(readLine()!)
}

let answer = notHeard.intersection(notSeen).sorted()

print(answer.count)
for ele in answer {
    print(ele)
}