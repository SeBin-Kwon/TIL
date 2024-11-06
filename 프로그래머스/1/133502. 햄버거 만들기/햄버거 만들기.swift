import Foundation

func solution(_ ingredient:[Int]) -> Int {
    var stack = [Int]()
    let recipe = [1, 2, 3, 1]
    var result = 0

    for i in ingredient {
        stack.append(i)

        if Array(stack.suffix(4)) == recipe {
            stack.removeLast(4)
            result += 1
        }
    }
    return result
}