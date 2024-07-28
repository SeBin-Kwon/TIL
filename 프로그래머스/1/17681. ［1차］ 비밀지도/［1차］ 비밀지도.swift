func solution(_ n: Int, _ arr1: [Int], _ arr2: [Int]) -> [String] {
    var answer: [String] = []

    for i in 0..<n {
        let binary = String(arr1[i] | arr2[i], radix: 2)
        let padded = String(repeating: "0", count: n - binary.count) + binary
        let row = padded.map { $0 == "0" ? " " : "#" }.joined()
        answer.append(row)
    }

    return answer
}