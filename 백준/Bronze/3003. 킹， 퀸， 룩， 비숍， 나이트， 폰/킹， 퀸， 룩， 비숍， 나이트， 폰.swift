let chess = [1, 1, 2, 2, 2, 8]
let input = readLine()!.split(separator: " ").map { Int($0)! }
var answer = Array(repeating: 0, count: 6)
for i in 0..<chess.count {
    answer[i] = chess[i] - input[i]
}
print(answer.map { String($0) }.joined(separator: " "))