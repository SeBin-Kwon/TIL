import Foundation

func solution(_ t:String, _ p:String) -> Int {
    
    let tArray = Array(t)
    var answer = 0
    let pNum = Int(p)!
    for i in 0...t.count-p.count {
        let tRange = tArray[i..<i+p.count]
        if let tNum = Int(String(tRange)) {
            if tNum <= pNum { answer += 1 }
        }
    }
    
    return answer
}