import Foundation

func solution(_ k:Int, _ score:[Int]) -> [Int] {
    var kArray = [Int]()
    var answer = [Int]()
    
    for s in score {
        if kArray.count < k {
            kArray.append(s)
        } else {
            if let minValue = kArray.first, minValue < s {
                kArray.removeFirst()
                kArray.append(s)
            }
        }
        kArray = kArray.sorted()
        answer.append(kArray.first ?? 0)
    }
    return answer
}