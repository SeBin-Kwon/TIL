import Foundation

func solution(_ keymap:[String], _ targets:[String]) -> [Int] {
    var alphaDict: [Character : Int] = [:]
    
    for string in keymap {
        for (index, char) in string.enumerated() {
            alphaDict[char] = min(alphaDict[char] ?? 100, index + 1)
        }
    }
    
    var ans:[Int] = Array(repeating: 0, count: targets.count)
    
    for (index, string) in targets.enumerated() {
        for char in string {
            guard let count = alphaDict[char] else {
                ans[index] = -1
                break
            }
            ans[index] += count
        }
        
    }

    return ans
}