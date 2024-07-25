import Foundation

func solution(_ d:[Int], _ budget:Int) -> Int {
    let array = d.sorted()
    var cnt = 0 
    var sum = 0
    for a in array {
        guard budget >= sum + a else { continue }
        sum += a
        cnt += 1
    }
    
    return cnt
}