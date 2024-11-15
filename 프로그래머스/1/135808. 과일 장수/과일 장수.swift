import Foundation

func solution(_ k:Int, _ m:Int, _ score:[Int]) -> Int {
    let s = score.sorted(by: >)
    return stride(from: m-1, to: score.count, by: m)
        .reduce(0) { r, e in
             r + s[e] * m 
        }
}