func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var failure = [Int: Double]()
    var total = Double(stages.count) // 8.0
    var countArr = Array(repeating: 0, count: N+2) // [0, 0, 0, 0, 0, 0]

    for num in stages {
        countArr[num] += 1 // [0, 1, 3, 2, 1, 0, 1]
    }

    for i in 1..<N+1 {
        if countArr[i] == 0 {
            failure[i] = 0.0
        } else {
            total = total - Double(countArr[i])
            failure[i] = Double(countArr[i]) / total
        }
    }
    let sortArr = failure.sorted(by: <).sorted(by: { $0.1 > $1.1 })
    let result = sortArr.map{ $0.key }

    return result
}