import Foundation

func solution(_ n:Int) -> Int {
    var x = 1
    while true {
        if n % x == 1 {
            break
        }
        x += 1
    }
    return x
}