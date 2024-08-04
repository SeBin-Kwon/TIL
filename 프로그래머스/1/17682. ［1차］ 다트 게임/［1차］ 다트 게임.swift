func solution(_ dartResult:String) -> Int {
    
    let dartArr = dartResult.replacingOccurrences(of: "10", with: "a").map { String($0) }
    
    let bonusDict = ["S": 1, "D": 2, "T": 3]
    
    var stack = [Int]()
    
    for ele in dartArr {
        if Int(ele) != nil || ele == "a" {
            if ele == "a" {
                stack.append(10)
            } else {
                stack.append(Int(ele)!)    
            }
        } else if bonusDict[ele] != nil {
            let point = stack.popLast()!
            stack.append(power(point, bonusDict[ele]!))
        } else if ele == "#" {
            let point = stack.popLast()!
            stack.append(point * -1)
        } else if ele == "*" {
            let point = stack.popLast()!
            if stack.count != 0 {
                let lastPoint = stack.popLast()!
                stack.append(lastPoint * 2)
            }
            stack.append(point * 2)
        }
    }
    
    return stack.reduce(0, +)
}

func power(_ n: Int, _ p: Int) -> Int {
    var sum = 1
    for _ in 1...p {
        sum *= n
    }
    return sum
}