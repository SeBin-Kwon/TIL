import Foundation

func solution(_ n:Int, _ m:Int, _ section:[Int]) -> Int {

    var painted = 0
    var ans = 0

    for s in section {
        if painted < s {
            painted = s + m - 1
            ans += 1
        }
    }

    return ans
}