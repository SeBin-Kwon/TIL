import Foundation

func solution(_ a:Int, _ b:Int, _ n:Int) -> Int {

    var answer = 0
    var empty = n
    var cola = 0
    var remain = 0
    while empty >= a {
        cola = empty / a * b
        answer += cola
        remain = empty % a
        empty = cola + remain
    }
    
    return answer
}