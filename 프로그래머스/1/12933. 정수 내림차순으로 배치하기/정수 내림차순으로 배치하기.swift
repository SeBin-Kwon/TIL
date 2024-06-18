func solution(_ n:Int64) -> Int64 {
    var array = String(n).map { String($0) }
    return Int64(array.sorted(by: >).joined())!
}