import Foundation

func solution(_ s:String) -> Bool
{
    // var answer: Bool = false
    var stack = [Character]()
    for i in s {
        if i == "(" {
            stack.append(i)
        } else {
            if stack.isEmpty {
                return false
            }
            stack.popLast()
        }
        // if stack.last == "(" && i == ")" {
        //     stack.popLast()
        // }
        // else if stack.isEmpty && i == ")" { 
        //     return answer
        // }
    }
    if stack.isEmpty {
        // answer = true
        return true        
    } else {
        return false
    }
}