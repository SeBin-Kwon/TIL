import Foundation

func solution(_ s: String) -> [Int] {
    var word: [String: Int] = [:]
    var result = [Int]()

    for (index, val) in Array(s).map { String($0) }.enumerated() {
        if let beforeIndex = word[val] {
            result.append(index - beforeIndex)
        } else {
            result.append(-1)
        }
        word[val] = index
    }
    return result
}