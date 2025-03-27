import Foundation

let strList = readLine()!.map { String($0) }
    
let alphabet = "abcdefghijklmnopqrstuvwxyz".map { String($0) }
var dict = [String: Int]()

alphabet.forEach {
    dict[$0] = 0
}
strList.forEach {
    dict[$0]! += 1
}

alphabet.forEach {
    print(dict[$0]!, terminator: " ")
}