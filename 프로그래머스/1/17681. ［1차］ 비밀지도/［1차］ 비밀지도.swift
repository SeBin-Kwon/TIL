func solution(_ n:Int, _ arr1:[Int], _ arr2:[Int]) -> [String] {
    var answer: [String] = []
    var binaryArr1 = [[Character]]()
    var binaryArr2 = [[Character]]()
    
    for i in 0..<n {
        var num1 = Array(String(arr1[i], radix: 2))
        var num2 = Array(String(arr2[i], radix: 2))
        if num1.count < n {
            let zero = Array(String(repeating: "0", count: n - num1.count))
            num1 = zero + num1
        }
        if num2.count < n {
            let zero = Array(String(repeating: "0", count: n - num2.count))
            num2 = zero + num2
        }
        binaryArr1.append(num1)
        binaryArr2.append(num2)
    }

    for i in 0..<n {
        var row = ""
        for j in 0..<n {
            if binaryArr1[i][j] == "0" && binaryArr2[i][j] == "0" {
                row += " "
            } else {
                row += "#"
            }
        }
        answer.append(row)
    }
    
    return answer
}