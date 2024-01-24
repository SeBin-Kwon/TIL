import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var width = [Int]()
    var height = [Int]()
    var answer = 1000000
    
    var sortSizes = sizes.map { size in
        size.sorted(by: >)
    }
    
    width = sortSizes.map { $0[0] }
    height = sortSizes.map { $0[1] }
    
    answer = width.max()! * height.max()!
    
    return answer
}