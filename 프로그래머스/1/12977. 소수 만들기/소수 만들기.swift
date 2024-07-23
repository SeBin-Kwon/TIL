import Foundation

func solution(_ nums:[Int]) -> Int {
    var answer = 0
    let combinationArray = combination(nums, 3)
    for com in combinationArray { 
        var flag = true
        let sum = com.reduce(0,+)
        for i in 2...sum/2 { 
            if sum % i == 0 {
                flag = false
                break 
            }
        }
        if flag {
            answer += 1
        }
    }
    return answer
}

func combination<T: Comparable>(_ array: [T], _ n: Int) -> [[T]] {
    var result = [[T]]()
    if array.count < n { return result }
    func cycle(_ index: Int, _ now: [T]) {
        if now.count == n {
            result.append(now)
            return
        }
        for i in index..<array.count {
            cycle(i + 1, now + [array[i]])
        }
    }
    cycle(0, [])
    return result
}