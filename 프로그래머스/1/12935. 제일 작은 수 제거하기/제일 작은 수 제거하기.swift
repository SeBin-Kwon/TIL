func solution(_ arr:[Int]) -> [Int] {
    var result = arr
    if result.count != 1 {
        result.remove(at: arr.firstIndex(of: arr.min()!)!)
    }
    return result.count == 1 ? [-1] : result
}