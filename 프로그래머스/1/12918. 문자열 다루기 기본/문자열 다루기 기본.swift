func solution(_ s:String) -> Bool {
    guard s.count == 4 || s.count == 6 else { return false }
    return Int(s) != nil ? true : false
}