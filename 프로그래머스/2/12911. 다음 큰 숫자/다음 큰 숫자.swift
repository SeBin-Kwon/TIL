import Foundation

func solution(_ n:Int) -> Int
{
    var answer = n
    let oneCount = String(n, radix: 2).filter { $0 == "1" }.count
    
    while true {
        answer += 1
        let nextCount = String(answer, radix: 2).filter { $0 == "1" }.count
        if answer > n && oneCount == nextCount {
            break
        }
    }

    return answer
}