import Foundation

func solution(_ s:String) -> Int {
    var x = ""
    var xCnt = 0
    var yCnt = 0
    var answer = 0
    var isFirst = true
    for c in s {
        if isFirst {
            x = String(c)
            xCnt += 1
            isFirst = false
        } else {
            if x == String(c) {
                xCnt += 1
            } else {
                yCnt += 1
            }
            if xCnt == yCnt {
                answer += 1
                x = ""
                xCnt = 0
                yCnt = 0
                isFirst = true
            }
        }
    }
    if xCnt != yCnt {
        answer += 1
    }
    
    return answer
}