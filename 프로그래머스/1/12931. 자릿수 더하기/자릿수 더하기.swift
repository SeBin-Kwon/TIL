import Foundation

func solution(_ n:Int) -> Int {
    var answer:Int = 0
    let str = String(n)
    
    for chr in str {
        answer += Int(String(chr))!
    }
    
    return answer
}