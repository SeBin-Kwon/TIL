import Foundation
let testCase = Int(readLine()!)!
for _ in 0..<testCase {
    var dict = [String: [String]]()
    var count = 1
    let n = Int(readLine()!)!
    for _ in 0..<n {
        let input = readLine()!.split(separator: " ").map(\.description)
        if dict[input[1]] != nil {
            dict[input[1]]?.append(input[0])
        } else {
            dict[input[1]] = [input[0]]
        }
    }
    for value in dict.values {
        count *= value.count + 1
    }
    print(count - 1)
}