import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var lostSet = Set(lost).subtracting(reserve)
    var reserveArray = Array(Set(reserve).subtracting(lost)).sorted(by: <)

    for reserve in reserveArray {
        if lostSet.contains(reserve - 1) {
            lostSet.remove(reserve - 1)
            continue
        }
        if lostSet.contains(reserve + 1) {
            lostSet.remove(reserve + 1)
        }
    }
    return (n - lostSet.count)
}