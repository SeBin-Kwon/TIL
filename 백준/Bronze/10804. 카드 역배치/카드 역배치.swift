import Foundation

var list = Array(1...20)
for _ in 0..<10 {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    let (a, b) = (input[0], input[1])
    let reversedList = list[a-1...b-1].reversed()
    list.replaceSubrange(a-1...b-1, with: reversedList)
}
for num in list {
    print(num, terminator: " ")
}