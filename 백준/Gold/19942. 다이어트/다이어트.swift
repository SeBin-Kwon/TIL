import Foundation

let n = Int(readLine()!)!
let input = readLine()!.split(separator: " ").map { Int($0)! }
let (mP, mF, mS, mV) = (input[0], input[1], input[2], input[3])
var food = [(p: Int, f: Int, s: Int, v: Int, c: Int)]()
var idxArr = [Int]()
var answer = [Int]()
var minCost = Int.max

for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    food.append((input[0], input[1], input[2], input[3], input[4]))
}

for i in 1...n {
    combi(i, 0)
}
if answer.isEmpty {
    print(-1)
} else {
    print(minCost)
    print(answer.map { String($0 + 1) }.joined(separator: " "))
}

func combi(_ k: Int, _ idx: Int) {
    if idxArr.count == k {
        var (p, f, s, v, cost) = (0, 0, 0, 0, 0)
        for i in 0..<k {
            p += food[idxArr[i]].p
            f += food[idxArr[i]].f
            s += food[idxArr[i]].s
            v += food[idxArr[i]].v
            cost += food[idxArr[i]].c
        }
        if p < mP || f < mF || s < mS || v < mV { return }
        if cost < minCost {
            minCost = cost
            answer = idxArr
        } else if cost == minCost {
            for i in 0..<min(answer.count, idxArr.count) {
                if idxArr[i] < answer[i] {
                    answer = idxArr
                    break
                } else if idxArr[i] > answer[i] {
                    break
                }
            }
        }
        return
    }
    for i in idx..<n {
        idxArr.append(i)
        combi(k, i + 1)
        idxArr.removeLast()
    }
}
