import Foundation

func solution(_ s:String, _ skip:String, _ index:Int) -> String {
    let alphabet = "abcdefghijklmnopqrstuvwxyz".filter { !skip.contains($0) }.map { String($0) }
    let string = s.map { String($0) }
    var answer = ""
    for s in string {
        if let first = alphabet.firstIndex(of: s) { 
            let num = (first + index) % alphabet.count
            answer += alphabet[num]
        }
    }
    return answer
}