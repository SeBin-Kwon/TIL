import Foundation

func solution(_ left:Int, _ right:Int) -> Int {
    var answer = 0
    
    for num in left...right {
        var cnt = 0
        for i in 1...num {
            if num % i == 0 {
                cnt += 1
            }
        }
        if cnt % 2 == 0 {
            answer += num
        } else {
            answer -= num
        }
    }
    
    return answer
}