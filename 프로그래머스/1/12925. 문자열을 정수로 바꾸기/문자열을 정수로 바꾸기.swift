func solution(_ s:String) -> Int {
    var str = s
    // let start = str.startIndex
    // let end = str.endIndex
    // if String(str[start]) == "+" {
    //     str = String(str[str.index(after: start)...end])
    // }
    return Int(str) ?? 0
}