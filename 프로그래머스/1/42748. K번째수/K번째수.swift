import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var answer = [Int]()
    for cmd in commands {
        var cutArray = Array(array[cmd[0]-1..<cmd[1]].sorted())
        answer.append(cutArray[cmd[2]-1])
    }
    return answer
}