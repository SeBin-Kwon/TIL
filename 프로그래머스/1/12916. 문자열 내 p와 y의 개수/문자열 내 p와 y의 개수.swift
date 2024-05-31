import Foundation

func solution(_ s:String) -> Bool
{
    var ans:Bool = false
    var pCnt = 0
    var yCnt = 0
    
    for i in s {
        if String(i).caseInsensitiveCompare("p") == .orderedSame {
            pCnt += 1
        } else if String(i).caseInsensitiveCompare("y") == .orderedSame {
            yCnt += 1
        }
    }

    return pCnt == yCnt ? !ans : ans
}