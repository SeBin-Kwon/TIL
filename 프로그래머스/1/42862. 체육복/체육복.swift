import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var lostSet:Set<Int> = Set(lost).subtracting(reserve)
    var reserveArray = Array(Set(reserve).subtracting(lost)).sorted(by: <)

    for i in reserveArray {

        if lostSet.contains(i - 1) {
            lostSet.remove(i - 1)
            continue
        }
        if lostSet.contains(i + 1) {
            lostSet.remove(i + 1)
        }
    }

    return (n - lostSet.count)
}