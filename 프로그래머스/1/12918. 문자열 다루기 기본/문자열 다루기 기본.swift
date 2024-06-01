func solution(_ s:String) -> Bool {
    guard s.count == 4 || s.count == 6 else { return false }
    
    for i in s {
        if let c = Int(String(i)) {
            continue
        }
        return false
    }
    return true
}