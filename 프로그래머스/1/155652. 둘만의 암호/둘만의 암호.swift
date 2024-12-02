import Foundation

func solution(_ s:String, _ skip:String, _ index:Int) -> String {
    let alphabet = "abcdefghijklmnopqrstuvwxyz".map { String($0) }
    var s = s.map { String($0) }
    
    for i in 0..<s.count {
        if var c = alphabet.firstIndex(of: s[i]) {
            var index = index
            
            while index != 0 {      
                c += 1
                c %= 26
                
                if skip.contains(alphabet[c]) { continue }
                
                index -= 1
                s[i] = alphabet[c]
            }
        }
    }
    return s.joined()
}