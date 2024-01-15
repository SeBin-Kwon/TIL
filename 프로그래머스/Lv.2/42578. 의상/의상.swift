import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var dic = [String:Int]()
    var answer = 1
    for c in clothes {
        dic[c[1], default: 0] += 1
    }
    for d in dic {
        answer *= d.value + 1
    }
    return answer - 1
}