func solution(_ s:String, _ n:Int) -> String {
    var answer = ""
    
    for char in s {
    guard char != " " else { 
        answer += " " 
        continue 
    }
    var asciiValue = Int(char.asciiValue!)
    
    switch asciiValue {
        case 65...90:
            asciiValue = (asciiValue + n - 65) % 26 + 65
        case 97...122:
            asciiValue = (asciiValue + n - 97) % 26 + 97
        default:
            break
    }
    answer += String(UnicodeScalar(asciiValue)!)   
}
    return answer
}