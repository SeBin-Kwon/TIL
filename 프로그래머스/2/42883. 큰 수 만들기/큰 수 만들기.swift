import Foundation

func solution(_ number:String, _ k:Int) -> String {
    var stack:[Character] = []
    var k = k

    for i in number {
        while let last = stack.last, last < i, k > 0 {
            k -= 1
            stack.removeLast()
        }
        stack.append(i)
    }

    return String(String(stack).prefix(stack.count - k))
}