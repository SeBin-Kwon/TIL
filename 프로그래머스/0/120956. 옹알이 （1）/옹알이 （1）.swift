import Foundation

func solution(_ babbling:[String]) -> Int {
    var dict = ["aya": 0, "ye": 0, "woo": 0, "ma": 0]
    var answer = 0
    var check = ""
    var flag = false
    
    for str in babbling {
        for cha in str {
            check += String(cha)
            if dict[check] != nil {
                check = ""
                flag = true
            } else {
                flag = false
            }
        }
        if flag {
            answer += 1
        }
        check = ""
    }
    
    return answer
}