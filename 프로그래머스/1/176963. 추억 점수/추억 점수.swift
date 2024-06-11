import Foundation

func solution(_ name:[String], _ yearning:[Int], _ photo:[[String]]) -> [Int] {
    var dict = [String:Int]()
    for i in 0..<name.count {
        dict[name[i]] = yearning[i]
    }
    return photo.map { $0.reduce(0) { $0 + (dict[$1] ?? 0) } }
}
